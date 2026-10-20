# Inspect the distribution of important iSign CI/CD duration metrics.
# This prepares the simple statistical baseline that will later be
# compared with Isolation Forest.

import pandas as pd


# ------------------------------------------------------------
# Load run-level and step-level data
# ------------------------------------------------------------

runs = pd.read_csv("data/raw/isign_frontend_runs.csv")
steps = pd.read_csv("data/raw/isign_frontend_steps.csv")


# Convert duration columns to numeric
runs["workflow_duration_seconds"] = pd.to_numeric(
    runs["workflow_duration_seconds"],
    errors="coerce",
)

runs["build_deploy_duration_seconds"] = pd.to_numeric(
    runs["build_deploy_duration_seconds"],
    errors="coerce",
)

steps["duration_seconds"] = pd.to_numeric(
    steps["duration_seconds"],
    errors="coerce",
)


# Get the SCP transfer duration from each successful run
scp = steps[
    (steps["step_name"] == "Transfer build files via SCP")
    & (steps["step_conclusion"] == "success")
]["duration_seconds"]


# ------------------------------------------------------------
# Calculate distribution statistics
# ------------------------------------------------------------

def describe_metric(name, values):

    values = values.dropna()

    q1 = values.quantile(0.25)
    median = values.median()
    q3 = values.quantile(0.75)
    iqr = q3 - q1

    print()
    print(name)
    print("-" * len(name))
    print(f"Observations : {len(values)}")
    print(f"Minimum      : {values.min():.2f} s")
    print(f"Q1           : {q1:.2f} s")
    print(f"Median       : {median:.2f} s")
    print(f"Q3           : {q3:.2f} s")
    print(f"IQR          : {iqr:.2f} s")
    print(f"Maximum      : {values.max():.2f} s")


describe_metric(
    "Workflow duration",
    runs["workflow_duration_seconds"],
)

describe_metric(
    "Build-and-deploy duration",
    runs["build_deploy_duration_seconds"],
)

describe_metric(
    "SCP transfer duration",
    scp,
)