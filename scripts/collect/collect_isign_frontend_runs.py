# Collect historical GitHub Actions data for the selected iSign frontend workflow.
# This script READS existing workflow history only.
# It does NOT trigger or modify any GitHub Actions workflow.

import csv
import json
import subprocess
from datetime import datetime
from pathlib import Path


# Selected thesis repository/workflow
REPO = "i3cubes/iSign_v3_FE"
WORKFLOW = "Deploy-to_Dev_Server.yml"
BRANCH = "development"


def gh_api(endpoint):
    """Call GitHub API through the already authenticated GitHub CLI."""

    result = subprocess.run(
        ["gh", "api", endpoint],
        capture_output=True,
        text=True,
        check=True,
    )

    return json.loads(result.stdout)


def duration_seconds(started_at, completed_at):
    """Calculate execution duration from GitHub timestamps."""

    if not started_at or not completed_at:
        return None

    start = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
    end = datetime.fromisoformat(completed_at.replace("Z", "+00:00"))

    return (end - start).total_seconds()


# -------------------------------------------------------------------
# 1. Get completed frontend push workflow runs
# -------------------------------------------------------------------

runs_response = gh_api(
    f"repos/{REPO}/actions/workflows/{WORKFLOW}/runs"
    f"?branch={BRANCH}&event=push&status=completed&per_page=100"
)

all_runs = runs_response["workflow_runs"]

print(f"Historical completed frontend runs found: {len(all_runs)}")


# Data that will be written to CSV
run_rows = []
step_rows = []


# -------------------------------------------------------------------
# 2. Inspect jobs inside every historical workflow run
# -------------------------------------------------------------------

for run in all_runs:

    run_id = run["id"]

    jobs_response = gh_api(
        f"repos/{REPO}/actions/runs/{run_id}/jobs?per_page=100"
    )

    jobs = jobs_response["jobs"]

    check_job = next(
        (job for job in jobs if job["name"] == "check-commit-message"),
        None,
    )

    build_job = next(
        (job for job in jobs if job["name"] == "build-and-deploy"),
        None,
    )

    # We want directly comparable full successful deployments.
    if not build_job or build_job["conclusion"] != "success":
        continue

    workflow_duration = duration_seconds(
    run.get("run_started_at"),
    run.get("updated_at"),
)

    check_duration = (
        duration_seconds(
            check_job.get("started_at"),
            check_job.get("completed_at"),
        )
        if check_job
        else None
    )

    build_duration = duration_seconds(
        build_job.get("started_at"),
        build_job.get("completed_at"),
    )

    # ----------------------------------------------------------------
    # 3. Store one row per comparable workflow run
    # ----------------------------------------------------------------

    run_rows.append(
    {
        "run_id": run_id,
        "run_number": run["run_number"],
        "run_attempt": run["run_attempt"],
        "event": run["event"],
        "branch": run["head_branch"],
        "head_sha": run["head_sha"],
        "created_at": run["created_at"],
        "run_started_at": run.get("run_started_at"),
        "updated_at": run["updated_at"],
        "run_conclusion": run["conclusion"],
        "workflow_duration_seconds": workflow_duration,
        "check_commit_duration_seconds": check_duration,
        "build_deploy_duration_seconds": build_duration,
    }
)

    # ----------------------------------------------------------------
    # 4. Store every step inside build-and-deploy
    # ----------------------------------------------------------------

    for step in build_job.get("steps", []):

        step_rows.append(
            {
                "run_id": run_id,
                "run_number": run["run_number"],
                "head_sha": run["head_sha"],
                "run_created_at": run["created_at"],
                "step_number": step["number"],
                "step_name": step["name"],
                "step_conclusion": step["conclusion"],
                "started_at": step["started_at"],
                "completed_at": step["completed_at"],
                "duration_seconds": duration_seconds(
                    step["started_at"],
                    step["completed_at"],
                ),
            }
        )


# -------------------------------------------------------------------
# 5. Save raw collected data locally
# -------------------------------------------------------------------

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

runs_file = output_dir / "isign_frontend_runs.csv"
steps_file = output_dir / "isign_frontend_steps.csv"


with runs_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=run_rows[0].keys())
    writer.writeheader()
    writer.writerows(run_rows)


with steps_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=step_rows[0].keys())
    writer.writeheader()
    writer.writerows(step_rows)


print()
print(f"Comparable successful full runs collected: {len(run_rows)}")
print(f"Step observations collected: {len(step_rows)}")
print(f"Run data saved to: {runs_file}")
print(f"Step data saved to: {steps_file}")