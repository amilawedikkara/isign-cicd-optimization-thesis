# Summarize run-level durations for the 33 comparable
# successful iSign frontend GitHub Actions workflow runs.

from pathlib import Path

import pandas as pd


INPUT_FILE = Path("data/raw/isign_frontend_runs.csv")
OUTPUT_FILE = Path("data/processed/isign_frontend_run_summary.csv")


# Load collected run-level data
df = pd.read_csv(INPUT_FILE)


duration_columns = [
    "workflow_duration_seconds",
    "check_commit_duration_seconds",
    "build_deploy_duration_seconds",
]


# Make sure duration values are numeric
for column in duration_columns:
    df[column] = pd.to_numeric(
        df[column],
        errors="coerce",
    )


rows = []


# Calculate descriptive statistics for each duration metric
for column in duration_columns:

    values = df[column].dropna()

    rows.append(
        {
            "metric": column,
            "observations": len(values),
            "mean_seconds": values.mean(),
            "median_seconds": values.median(),
            "std_seconds": values.std(),
            "min_seconds": values.min(),
            "max_seconds": values.max(),
        }
    )


summary = pd.DataFrame(rows)


numeric_columns = [
    "mean_seconds",
    "median_seconds",
    "std_seconds",
    "min_seconds",
    "max_seconds",
]

summary[numeric_columns] = summary[numeric_columns].round(2)


# Save processed baseline statistics
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

summary.to_csv(
    OUTPUT_FILE,
    index=False,
)


print(f"Comparable workflow runs loaded: {len(df)}")
print()
print("Run-level baseline summary:")
print()
print(summary.to_string(index=False))
print()
print(f"Summary saved to: {OUTPUT_FILE}")