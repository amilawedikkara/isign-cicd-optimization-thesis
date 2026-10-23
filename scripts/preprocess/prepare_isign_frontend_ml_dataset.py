from pathlib import Path
import pandas as pd


# ---------------------------------------------------------
# File locations
# ---------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "isign_frontend_steps.csv"
)

OUTPUT_FILE = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "isign_frontend_ml_dataset.csv"
)


# ---------------------------------------------------------
# Initial Isolation Forest feature set
#
# These steps:
# - occur in all 33 comparable runs
# - have no missing durations
# - have meaningful timing variation
# ---------------------------------------------------------

SELECTED_STEPS = [
    "Build appleboy/scp-action@v0.1.7",
    "Setup Node.js",
    "Install dependencies",
    "Build React app",
    "Transfer build files via SCP",
]


def main():
    # Load raw step-level GitHub Actions data
    df = pd.read_csv(INPUT_FILE)

    # Keep only the five selected successful steps
    selected = df[
        (df["step_name"].isin(SELECTED_STEPS))
        & (df["step_conclusion"] == "success")
    ].copy()

    # Convert duration to numeric values
    selected["duration_seconds"] = pd.to_numeric(
        selected["duration_seconds"],
        errors="coerce",
    )

    # -----------------------------------------------------
    # Validation
    # -----------------------------------------------------

    # We expect 33 comparable workflow runs
    run_count = selected["run_number"].nunique()

    if run_count != 33:
        raise ValueError(
            f"Expected 33 comparable runs, found {run_count}"
        )

    # Each run must contain exactly the five selected steps
    feature_counts = (
        selected.groupby("run_number")["step_name"]
        .nunique()
    )

    if not (feature_counts == len(SELECTED_STEPS)).all():
        raise ValueError(
            "At least one run does not contain all selected features."
        )

    # No selected duration may be missing
    if selected["duration_seconds"].isna().any():
        raise ValueError(
            "Missing duration found in selected features."
        )

    # -----------------------------------------------------
    # Convert long-format data to wide-format ML data
    #
    # Before:
    # run 55 | Setup Node.js | 8
    # run 55 | Build React app | 7
    #
    # After:
    # run_number | setup_node | build_react | ...
    # -----------------------------------------------------

    ml_dataset = selected.pivot(
        index="run_number",
        columns="step_name",
        values="duration_seconds",
    ).reset_index()

    # Rename columns to simple machine-friendly names
    ml_dataset = ml_dataset.rename(
        columns={
            "Build appleboy/scp-action@v0.1.7": "scp_action_setup_seconds",
            "Setup Node.js": "setup_node_seconds",
            "Install dependencies": "install_dependencies_seconds",
            "Build React app": "build_react_seconds",
            "Transfer build files via SCP": "scp_transfer_seconds",
        }
    )

    # Put columns in a clear fixed order
    ml_dataset = ml_dataset[
        [
            "run_number",
            "scp_action_setup_seconds",
            "setup_node_seconds",
            "install_dependencies_seconds",
            "build_react_seconds",
            "scp_transfer_seconds",
        ]
    ]

    # Sort runs numerically
    ml_dataset = ml_dataset.sort_values("run_number")

    # Save processed dataset
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    ml_dataset.to_csv(
        OUTPUT_FILE,
        index=False,
    )

    print(f"Created: {OUTPUT_FILE}")
    print(f"Runs: {len(ml_dataset)}")
    print()
    print(ml_dataset.to_string(index=False))


if __name__ == "__main__":
    main()