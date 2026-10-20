# scripts/baseline_method/detect_iqr_anomalies.py

from pathlib import Path
import pandas as pd


# ---------------------------------------------------------
# File paths
# ---------------------------------------------------------

RUNS_FILE = Path("data/raw/isign_frontend_runs.csv")
STEPS_FILE = Path("data/raw/isign_frontend_steps.csv")

OUTPUT_FILE = Path("data/processed/isign_frontend_iqr_anomalies.csv")
THRESHOLDS_FILE = Path("data/processed/isign_frontend_iqr_thresholds.csv")


# ---------------------------------------------------------
# Helper function
# ---------------------------------------------------------

def calculate_iqr_threshold(series):
    """
    Calculate the upper IQR outlier threshold.

    Upper threshold = Q3 + 1.5 * IQR
    IQR = Q3 - Q1
    """

    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1

    upper_threshold = q3 + 1.5 * iqr

    return q1, q3, iqr, upper_threshold


# ---------------------------------------------------------
# Load data
# ---------------------------------------------------------

runs = pd.read_csv(RUNS_FILE)
steps = pd.read_csv(STEPS_FILE)


# ---------------------------------------------------------
# Extract SCP transfer duration for each run
# ---------------------------------------------------------

scp_steps = steps[
    (steps["step_name"] == "Transfer build files via SCP")
    & (steps["step_conclusion"] == "success")
][
    ["run_id", "run_number", "duration_seconds"]
].copy()

scp_steps = scp_steps.rename(
    columns={"duration_seconds": "scp_duration_seconds"}
)


# ---------------------------------------------------------
# Add SCP duration to the run-level dataset
# ---------------------------------------------------------

analysis = runs.merge(
    scp_steps,
    on=["run_id", "run_number"],
    how="left"
)


# ---------------------------------------------------------
# Metrics we want to examine
# ---------------------------------------------------------

metrics = {
    "workflow_duration_seconds": "workflow",
    "build_deploy_duration_seconds": "build_deploy",
    "scp_duration_seconds": "scp",
}


threshold_records = []


# ---------------------------------------------------------
# Calculate IQR threshold and anomaly flag for each metric
# ---------------------------------------------------------

for column, short_name in metrics.items():

    q1, q3, iqr, upper_threshold = calculate_iqr_threshold(
        analysis[column].dropna()
    )

    # A value above the upper IQR fence is treated as
    # a candidate slow-duration anomaly.
    analysis[f"{short_name}_iqr_anomaly"] = (
        analysis[column] > upper_threshold
    )

    threshold_records.append(
        {
            "metric": column,
            "q1": q1,
            "q3": q3,
            "iqr": iqr,
            "upper_threshold": upper_threshold,
        }
    )


# ---------------------------------------------------------
# Overall anomaly flag
# ---------------------------------------------------------

analysis["any_iqr_anomaly"] = (
    analysis["workflow_iqr_anomaly"]
    | analysis["build_deploy_iqr_anomaly"]
    | analysis["scp_iqr_anomaly"]
)


# ---------------------------------------------------------
# Keep only runs flagged by at least one metric
# ---------------------------------------------------------

anomalies = analysis[
    analysis["any_iqr_anomaly"]
].copy()


# ---------------------------------------------------------
# Save results
# ---------------------------------------------------------

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

anomalies.to_csv(OUTPUT_FILE, index=False)

thresholds = pd.DataFrame(threshold_records)
thresholds.to_csv(THRESHOLDS_FILE, index=False)


# ---------------------------------------------------------
# Print threshold summary
# ---------------------------------------------------------

print("\nIQR THRESHOLDS")
print("-" * 70)

print(
    thresholds[
        ["metric", "q1", "q3", "iqr", "upper_threshold"]
    ].to_string(index=False)
)


# ---------------------------------------------------------
# Print flagged runs
# ---------------------------------------------------------

print("\nFLAGGED RUNS")
print("-" * 70)

if anomalies.empty:
    print("No IQR anomalies found.")
else:
    columns_to_show = [
        "run_number",
        "run_attempt",
        "workflow_duration_seconds",
        "build_deploy_duration_seconds",
        "scp_duration_seconds",
        "workflow_iqr_anomaly",
        "build_deploy_iqr_anomaly",
        "scp_iqr_anomaly",
    ]

    print(
        anomalies[
            columns_to_show
        ]
        .sort_values(
            by="workflow_duration_seconds",
            ascending=False
        )
        .to_string(index=False)
    )


print("\nSUMMARY")
print("-" * 70)

print(f"Comparable runs analysed: {len(analysis)}")
print(f"Runs flagged by IQR method: {len(anomalies)}")

print(
    "Workflow anomalies:",
    int(analysis["workflow_iqr_anomaly"].sum())
)

print(
    "Build-and-deploy anomalies:",
    int(analysis["build_deploy_iqr_anomaly"].sum())
)

print(
    "SCP anomalies:",
    int(analysis["scp_iqr_anomaly"].sum())
)

print(f"\nSaved: {OUTPUT_FILE}")
print(f"Saved: {THRESHOLDS_FILE}")