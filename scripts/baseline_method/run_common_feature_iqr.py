from pathlib import Path
import pandas as pd

INPUT = Path("data/processed/isign_frontend_ml_dataset.csv")

THRESHOLDS_OUT = Path(
    "data/processed/isign_frontend_common_feature_iqr_thresholds.csv"
)

RESULTS_OUT = Path(
    "data/processed/isign_frontend_common_feature_iqr_results.csv"
)

FEATURES = [
    "scp_action_setup_seconds",
    "setup_node_seconds",
    "install_dependencies_seconds",
    "build_react_seconds",
    "scp_transfer_seconds",
]

# ------------------------------------------------------------
# 1. Load same dataset used for Isolation Forest
# ------------------------------------------------------------

if not INPUT.exists():
    raise FileNotFoundError(f"Missing input file: {INPUT}")

df = pd.read_csv(INPUT)

# ------------------------------------------------------------
# 2. Verify the exact same five features exist
# ------------------------------------------------------------

missing = [feature for feature in FEATURES if feature not in df.columns]

if missing:
    raise ValueError(
        f"Missing required features: {missing}\n"
        f"Available columns: {list(df.columns)}"
    )

# ------------------------------------------------------------
# 3. Find run identifier
# ------------------------------------------------------------

if "run_number" in df.columns:
    RUN_COL = "run_number"
elif "run_id" in df.columns:
    RUN_COL = "run_id"
else:
    raise ValueError(
        "No run_number or run_id column found.\n"
        f"Available columns: {list(df.columns)}"
    )

# ------------------------------------------------------------
# 4. Safety check: thesis dataset must contain 33 runs
# ------------------------------------------------------------

if len(df) != 33:
    raise ValueError(
        f"Expected 33 comparable iSign runs, but found {len(df)}."
    )

# Make sure features are numeric
for feature in FEATURES:
    df[feature] = pd.to_numeric(df[feature], errors="raise")

# ------------------------------------------------------------
# 5. Calculate IQR lower and upper fences for each feature
# ------------------------------------------------------------

threshold_rows = []
flag_columns = []

for feature in FEATURES:

    q1 = df[feature].quantile(0.25)
    q3 = df[feature].quantile(0.75)

    iqr = q3 - q1

    lower_fence = q1 - (1.5 * iqr)
    upper_fence = q3 + (1.5 * iqr)

    flag_col = f"iqr_flag_{feature}"

    df[flag_col] = (
        (df[feature] < lower_fence)
        |
        (df[feature] > upper_fence)
    )

    flag_columns.append(flag_col)

    threshold_rows.append(
        {
            "feature": feature,
            "q1_seconds": q1,
            "q3_seconds": q3,
            "iqr_seconds": iqr,
            "lower_fence_seconds": lower_fence,
            "upper_fence_seconds": upper_fence,
        }
    )

# ------------------------------------------------------------
# 6. Run-level IQR classification
# A run is anomalous if at least one of the five features
# crosses its lower OR upper IQR fence
# ------------------------------------------------------------

df["iqr_common_feature_anomaly"] = df[flag_columns].any(axis=1)

df["iqr_common_feature_flag_count"] = df[flag_columns].sum(axis=1)


def get_flagged_features(row):

    flagged = []

    for feature in FEATURES:

        flag_col = f"iqr_flag_{feature}"

        if bool(row[flag_col]):
            flagged.append(feature)

    return ";".join(flagged)


df["iqr_common_feature_flagged_features"] = df.apply(
    get_flagged_features,
    axis=1
)

# ------------------------------------------------------------
# 7. Save thresholds
# ------------------------------------------------------------

thresholds = pd.DataFrame(threshold_rows)

thresholds.to_csv(
    THRESHOLDS_OUT,
    index=False
)

# ------------------------------------------------------------
# 8. Save per-run results
# ------------------------------------------------------------

output_columns = (
    [RUN_COL]
    + FEATURES
    + flag_columns
    + [
        "iqr_common_feature_anomaly",
        "iqr_common_feature_flag_count",
        "iqr_common_feature_flagged_features",
    ]
)

df[output_columns].to_csv(
    RESULTS_OUT,
    index=False
)

# ------------------------------------------------------------
# 9. Print results
# ------------------------------------------------------------

print()
print("COMMON-FEATURE IQR ANALYSIS COMPLETE")
print("------------------------------------")

print(f"Runs analysed: {len(df)}")

print()
print("IQR thresholds:")
print(thresholds.to_string(index=False))

print()
print("Flagged runs:")

flagged_runs = df.loc[
    df["iqr_common_feature_anomaly"],
    [
        RUN_COL,
        "iqr_common_feature_flag_count",
        "iqr_common_feature_flagged_features",
    ],
].sort_values(RUN_COL)

if flagged_runs.empty:
    print("No runs flagged.")
else:
    print(flagged_runs.to_string(index=False))

print()
print("Files created:")
print(THRESHOLDS_OUT)
print(RESULTS_OUT)
