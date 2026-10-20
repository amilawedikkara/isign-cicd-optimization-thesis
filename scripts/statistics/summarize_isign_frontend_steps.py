# Summarize step durations across the 33 comparable
# successful iSign frontend build-and-deploy workflow runs.

from pathlib import Path

import pandas as pd


INPUT_FILE = Path("data/raw/isign_frontend_steps.csv")
OUTPUT_FILE = Path("data/processed/isign_frontend_step_summary.csv")


# ------------------------------------------------------------
# 1. Load collected GitHub Actions step data
# ------------------------------------------------------------

df = pd.read_csv(INPUT_FILE)

df["duration_seconds"] = pd.to_numeric(
    df["duration_seconds"],
    errors="coerce",
)


print(f"Step observations loaded: {len(df)}")
print(f"Unique workflow runs: {df['run_id'].nunique()}")


# ------------------------------------------------------------
# 2. Keep executed successful steps for timing analysis
#
# Skipped steps, such as "Notify on failure", should not be
# interpreted as unusually fast execution.
# ------------------------------------------------------------

executed = df[
    df["step_conclusion"] == "success"
].copy()


# ------------------------------------------------------------
# 3. Calculate descriptive statistics for each step
# ------------------------------------------------------------

summary = (
    executed
    .groupby("step_name")["duration_seconds"]
    .agg(
        observations="count",
        mean_seconds="mean",
        median_seconds="median",
        std_seconds="std",
        min_seconds="min",
        max_seconds="max",
    )
    .reset_index()
)


# Round values for easier reading
numeric_columns = [
    "mean_seconds",
    "median_seconds",
    "std_seconds",
    "min_seconds",
    "max_seconds",
]

summary[numeric_columns] = summary[numeric_columns].round(2)


# Rank steps by typical duration
summary = summary.sort_values(
    by="median_seconds",
    ascending=False,
)


# ------------------------------------------------------------
# 4. Save processed summary
# ------------------------------------------------------------

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

summary.to_csv(
    OUTPUT_FILE,
    index=False,
)


# ------------------------------------------------------------
# 5. Display results
# ------------------------------------------------------------

print()
print("Step duration summary:")
print()

print(
    summary.to_string(
        index=False
    )
)

print()
print(f"Summary saved to: {OUTPUT_FILE}")