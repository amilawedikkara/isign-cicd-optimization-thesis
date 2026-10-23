from pathlib import Path

import pandas as pd
from sklearn.ensemble import IsolationForest


# ---------------------------------------------------------
# File locations
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "isign_frontend_ml_dataset.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "isign_frontend_isolation_forest_results.csv"
)


# ---------------------------------------------------------
# Isolation Forest features
#
# run_number is NOT included because it is only an
# identifier, not a performance measurement.
# ---------------------------------------------------------

FEATURES = [
    "scp_action_setup_seconds",
    "setup_node_seconds",
    "install_dependencies_seconds",
    "build_react_seconds",
    "scp_transfer_seconds",
]


def main():
    # Load the prepared 33-run ML dataset
    df = pd.read_csv(INPUT_FILE)

    # -----------------------------------------------------
    # Validate input data
    # -----------------------------------------------------

    if len(df) != 33:
        raise ValueError(
            f"Expected 33 workflow runs, found {len(df)}"
        )

    missing_columns = [
        column for column in FEATURES
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required feature columns: {missing_columns}"
        )

    if df[FEATURES].isna().any().any():
        raise ValueError(
            "Missing values found in Isolation Forest features."
        )

    # X contains only the numerical performance features.
    # run_number is deliberately excluded.
    X = df[FEATURES]

    # -----------------------------------------------------
    # Isolation Forest configuration
    # -----------------------------------------------------
    #
    # n_estimators=100
    #   Scikit-learn default.
    #   Builds 100 isolation trees.
    #
    # contamination="auto"
    #   Does not force the model to find the same number
    #   of anomalies as the IQR method.
    #
    # random_state=42
    #   Fixed seed so the experiment is reproducible.
    #   The number 42 itself has no special mathematical
    #   meaning.
    # -----------------------------------------------------

    model = IsolationForest(
        n_estimators=100,
        contamination="auto",
        random_state=42,
    )

    # Train the model using the 5 timing features
    model.fit(X)

    # -----------------------------------------------------
    # Generate results
    # -----------------------------------------------------

    results = df.copy()

    # score_samples:
    # lower value = more unusual observation
    results["if_score"] = model.score_samples(X)

    # decision_function:
    # negative value = model considers it anomalous
    # positive value = model considers it normal
    results["if_decision"] = model.decision_function(X)

    # predict:
    # -1 = anomaly
    #  1 = normal / inlier
    results["if_label"] = model.predict(X)

    results["if_is_anomaly"] = (
        results["if_label"] == -1
    )

    # Rank the most unusual runs first.
    # Lower score_samples value means more abnormal.
    results = results.sort_values(
        "if_score",
        ascending=True,
    )

    # -----------------------------------------------------
    # Save results
    # -----------------------------------------------------

    OUTPUT_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    results.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    # -----------------------------------------------------
    # Console summary
    # -----------------------------------------------------

    anomaly_count = int(
        results["if_is_anomaly"].sum()
    )

    print(f"Input runs: {len(results)}")
    print(f"Features: {len(FEATURES)}")
    print(f"Isolation Forest anomalies: {anomaly_count}")
    print()

    print("Runs ranked from most unusual to least unusual:")
    print()

    print(
        results[
            [
                "run_number",
                "if_score",
                "if_decision",
                "if_label",
                "scp_action_setup_seconds",
                "setup_node_seconds",
                "install_dependencies_seconds",
                "build_react_seconds",
                "scp_transfer_seconds",
            ]
        ].to_string(index=False)
    )

    print()
    print(f"Created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()