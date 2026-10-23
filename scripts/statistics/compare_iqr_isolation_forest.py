from pathlib import Path

import pandas as pd


# ---------------------------------------------------------
# File locations
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

ML_DATASET_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "isign_frontend_ml_dataset.csv"
)

IQR_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "isign_frontend_iqr_anomalies.csv"
)

IF_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "isign_frontend_isolation_forest_results.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "isign_frontend_method_comparison.csv"
)


def main():
    # -----------------------------------------------------
    # Load all 33 comparable workflow runs
    # -----------------------------------------------------

    base = pd.read_csv(ML_DATASET_FILE)[["run_number"]].copy()

    if len(base) != 33:
        raise ValueError(
            f"Expected 33 comparable runs, found {len(base)}"
        )

    # -----------------------------------------------------
    # IQR results
    #
    # The IQR anomaly file contains only runs that were
    # flagged by at least one IQR threshold.
    # -----------------------------------------------------

    iqr = pd.read_csv(IQR_FILE)

    iqr_columns = [
        "run_number",
        "workflow_iqr_anomaly",
        "build_deploy_iqr_anomaly",
        "scp_iqr_anomaly",
        "any_iqr_anomaly",
    ]

    iqr = iqr[iqr_columns].copy()

    # -----------------------------------------------------
    # Isolation Forest results
    # -----------------------------------------------------

    isolation_forest = pd.read_csv(IF_FILE)[
        [
            "run_number",
            "if_score",
            "if_decision",
            "if_label",
            "if_is_anomaly",
        ]
    ].copy()

    # -----------------------------------------------------
    # Merge methods onto the complete 33-run dataset
    # -----------------------------------------------------

    comparison = base.merge(
        iqr,
        on="run_number",
        how="left",
    )

    comparison = comparison.merge(
        isolation_forest,
        on="run_number",
        how="left",
    )

    # Runs not present in the IQR anomaly file were not
    # flagged by the IQR method.
    iqr_bool_columns = [
        "workflow_iqr_anomaly",
        "build_deploy_iqr_anomaly",
        "scp_iqr_anomaly",
        "any_iqr_anomaly",
    ]

    comparison[iqr_bool_columns] = (
        comparison[iqr_bool_columns]
        .fillna(False)
        .astype(bool)
    )

    # Ensure Isolation Forest flag is Boolean.
    comparison["if_is_anomaly"] = (
        comparison["if_label"] == -1
    )

    # -----------------------------------------------------
    # Classify the relationship between the two methods
    # -----------------------------------------------------

    def classify(row):
        iqr_flag = row["any_iqr_anomaly"]
        if_flag = row["if_is_anomaly"]

        if iqr_flag and if_flag:
            return "both"
        if iqr_flag and not if_flag:
            return "iqr_only"
        if not iqr_flag and if_flag:
            return "isolation_forest_only"

        return "normal_by_both"

    comparison["comparison_group"] = comparison.apply(
        classify,
        axis=1,
    )

    # Rank by Isolation Forest score:
    # lower score = more unusual.
    comparison = comparison.sort_values(
        ["comparison_group", "if_score"],
        ascending=[True, True],
    )

    # -----------------------------------------------------
    # Save comparison
    # -----------------------------------------------------

    comparison.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    # -----------------------------------------------------
    # Console summary
    # -----------------------------------------------------

    print("Method comparison")
    print("-----------------")
    print(f"Total comparable runs: {len(comparison)}")
    print()

    counts = (
        comparison["comparison_group"]
        .value_counts()
    )

    for group in [
        "both",
        "iqr_only",
        "isolation_forest_only",
        "normal_by_both",
    ]:
        print(
            f"{group}: {counts.get(group, 0)}"
        )

    print()

    for group in [
        "both",
        "iqr_only",
        "isolation_forest_only",
    ]:
        runs = (
            comparison.loc[
                comparison["comparison_group"] == group,
                "run_number",
            ]
            .astype(int)
            .sort_values()
            .tolist()
        )

        print(f"{group} runs: {runs}")

    print()
    print("Detailed flagged-run comparison:")
    print()

    flagged = comparison[
        comparison["comparison_group"]
        != "normal_by_both"
    ]

    print(
        flagged[
            [
                "run_number",
                "comparison_group",
                "workflow_iqr_anomaly",
                "build_deploy_iqr_anomaly",
                "scp_iqr_anomaly",
                "if_score",
                "if_label",
            ]
        ].to_string(index=False)
    )

    print()
    print(f"Created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()