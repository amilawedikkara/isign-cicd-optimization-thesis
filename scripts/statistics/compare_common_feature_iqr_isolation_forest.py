from pathlib import Path
import pandas as pd

IQR_FILE = Path(
    "data/processed/isign_frontend_common_feature_iqr_results.csv"
)

IF_FILE = Path(
    "data/processed/isign_frontend_isolation_forest_results.csv"
)

OUT_FILE = Path(
    "data/processed/isign_frontend_common_feature_method_comparison.csv"
)

# ------------------------------------------------------------
# 1. Load files
# ------------------------------------------------------------

if not IQR_FILE.exists():
    raise FileNotFoundError(f"Missing IQR file: {IQR_FILE}")

if not IF_FILE.exists():
    raise FileNotFoundError(f"Missing Isolation Forest file: {IF_FILE}")

iqr = pd.read_csv(IQR_FILE)
iso = pd.read_csv(IF_FILE)

# ------------------------------------------------------------
# 2. Detect run identifier
# ------------------------------------------------------------

def detect_run_col(df, name):
    for candidate in ["run_number", "run_id"]:
        if candidate in df.columns:
            return candidate

    raise ValueError(
        f"No run identifier found in {name}. "
        f"Columns: {list(df.columns)}"
    )

iqr_run_col = detect_run_col(iqr, "IQR file")
if_run_col = detect_run_col(iso, "Isolation Forest file")

# ------------------------------------------------------------
# 3. Validate 33 comparable runs
# ------------------------------------------------------------

if len(iqr) != 33:
    raise ValueError(
        f"Expected 33 IQR rows, found {len(iqr)}."
    )

if len(iso) != 33:
    raise ValueError(
        f"Expected 33 Isolation Forest rows, found {len(iso)}."
    )

# ------------------------------------------------------------
# 4. Detect Isolation Forest anomaly column safely
# ------------------------------------------------------------

if "if_anomaly" in iso.columns:
    iso["_if_anomaly_final"] = iso["if_anomaly"].astype(bool)

elif "is_anomaly" in iso.columns:
    iso["_if_anomaly_final"] = iso["is_anomaly"].astype(bool)

elif "if_label" in iso.columns:
    iso["_if_anomaly_final"] = iso["if_label"].astype(int).eq(-1)

elif "prediction" in iso.columns:
    iso["_if_anomaly_final"] = iso["prediction"].astype(int).eq(-1)

else:
    raise ValueError(
        "Could not identify Isolation Forest anomaly column.\n"
        f"Available columns: {list(iso.columns)}"
    )

# ------------------------------------------------------------
# 5. Prepare IQR classification
# ------------------------------------------------------------

if "iqr_common_feature_anomaly" not in iqr.columns:
    raise ValueError(
        "Missing iqr_common_feature_anomaly column."
    )

iqr["_iqr_anomaly_final"] = (
    iqr["iqr_common_feature_anomaly"]
    .astype(str)
    .str.lower()
    .map({"true": True, "false": False})
)

if iqr["_iqr_anomaly_final"].isna().any():
    # fallback if pandas already read booleans
    iqr["_iqr_anomaly_final"] = (
        iqr["iqr_common_feature_anomaly"].astype(bool)
    )

# ------------------------------------------------------------
# 6. Merge same 33 runs
# ------------------------------------------------------------

comparison = iqr[
    [
        iqr_run_col,
        "iqr_common_feature_anomaly",
        "iqr_common_feature_flag_count",
        "iqr_common_feature_flagged_features",
        "_iqr_anomaly_final",
    ]
].copy()

comparison = comparison.rename(
    columns={iqr_run_col: "run_number"}
)

if_cols = [if_run_col, "_if_anomaly_final"]

for optional in ["if_score", "if_decision", "if_label"]:
    if optional in iso.columns:
        if_cols.append(optional)

iso_small = iso[if_cols].copy()

iso_small = iso_small.rename(
    columns={if_run_col: "run_number"}
)

comparison = comparison.merge(
    iso_small,
    on="run_number",
    how="inner",
    validate="one_to_one"
)

if len(comparison) != 33:
    raise ValueError(
        f"Merged comparison has {len(comparison)} runs instead of 33."
    )

# ------------------------------------------------------------
# 7. Create comparison group
# ------------------------------------------------------------

def classify(row):
    iqr_flag = bool(row["_iqr_anomaly_final"])
    if_flag = bool(row["_if_anomaly_final"])

    if iqr_flag and if_flag:
        return "both"

    if iqr_flag and not if_flag:
        return "iqr_only"

    if not iqr_flag and if_flag:
        return "isolation_forest_only"

    return "normal_both"


comparison["comparison_group"] = comparison.apply(
    classify,
    axis=1
)

# ------------------------------------------------------------
# 8. Save clean comparison output
# ------------------------------------------------------------

comparison = comparison.drop(
    columns=[
        "_iqr_anomaly_final",
        "_if_anomaly_final",
    ]
)

comparison = comparison.sort_values("run_number")

comparison.to_csv(
    OUT_FILE,
    index=False
)

# ------------------------------------------------------------
# 9. Print exact results
# ------------------------------------------------------------

print()
print("COMMON-FEATURE METHOD COMPARISON COMPLETE")
print("-----------------------------------------")

print(f"Runs compared: {len(comparison)}")

print()
print("Group counts:")
print(
    comparison["comparison_group"]
    .value_counts()
    .reindex(
        [
            "both",
            "iqr_only",
            "isolation_forest_only",
            "normal_both",
        ],
        fill_value=0,
    )
)

print()
print("Runs by group:")

for group in [
    "both",
    "iqr_only",
    "isolation_forest_only",
    "normal_both",
]:
    runs = comparison.loc[
        comparison["comparison_group"] == group,
        "run_number",
    ].tolist()

    print(f"{group}: {runs}")

print()
print("Detailed non-normal runs:")

detail_cols = [
    "run_number",
    "comparison_group",
    "iqr_common_feature_flag_count",
    "iqr_common_feature_flagged_features",
]

for optional in ["if_score", "if_decision", "if_label"]:
    if optional in comparison.columns:
        detail_cols.append(optional)

print(
    comparison.loc[
        comparison["comparison_group"] != "normal_both",
        detail_cols,
    ].to_string(index=False)
)

print()
print(f"Saved: {OUT_FILE}")
