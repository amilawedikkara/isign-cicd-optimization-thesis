# iSign GitHub Actions Data Availability

Last verified: 15 October 2026

## Frontend
Repository: i3cubes/iSign_v3_FE
Workflow: .github/workflows/Deploy-to_Dev_Server.yml
Branch trigger: development
Total historical workflow runs: 55

## Backend
Repository: i3cubes/iSign_v3_BE
Workflow: .github/workflows/deploy_server.yml
Branch trigger: main
Total historical workflow runs: 134

## Important
These are total workflow-run counts, not yet the number of usable or structurally comparable runs.
Job-level filtering and workflow-version consistency still need to be checked before deciding how many runs are suitable for analysis.

## Verification Commands
Frontend: gh api "repos/i3cubes/iSign_v3_FE/actions/workflows/Deploy-to_Dev_Server.yml/runs?per_page=1" --jq '.total_count'
Backend: gh api "repos/i3cubes/iSign_v3_BE/actions/workflows/deploy_server.yml/runs?per_page=1" --jq '.total_count'

## Previously Verified Backend Run Breakdown

Total backend workflow runs: 134

Trigger/branch breakdown:
- 132 push runs on main
- 1 workflow_dispatch run on main
- 1 workflow_dispatch run on feature/database-foundation

For the 132 push/main runs, job outcomes were:

- 103: check-commit-message = success, build-and-deploy = success
- 21: check-commit-message = success, build-and-deploy = skipped
- 7: check-commit-message = success, build-and-deploy = failure
- 1: check-commit-message = failure, build-and-deploy = skipped

Interpretation:
The backend has a larger historical dataset than the frontend, but not every run performs the same work. Runs where build-and-deploy was skipped should not automatically be compared with full deployment runs.

## Verified Frontend Run Breakdown

Total frontend workflow runs: 55

Trigger/branch breakdown:
- 55 push runs on development

Interpretation:
All frontend workflow runs use the same event type and branch, which improves comparability at the trigger/branch level. Job-level execution still needs to be checked because some runs may skip build-and-deploy depending on the commit-message condition.

### Frontend Job-Level Breakdown

For the 55 push/development runs:

- 33: check-commit-message = success, build-and-deploy = success
- 22: check-commit-message = success, build-and-deploy = skipped

Interpretation:
Only 33 of the 55 frontend runs executed the full build-and-deploy job.
The 22 skipped runs should not automatically be compared with full deployment runs when analyzing execution time.

## Workflow Version Stability

Frontend:
- Workflow file: .github/workflows/Deploy-to_Dev_Server.yml
- Git history shows one workflow-file commit:
  - 3abf6d2, 17 May 2026, Deploy to server
- Interpretation: frontend workflow structure appears stable across its recorded history.

Backend:
- Workflow file: .github/workflows/deploy_server.yml
- Git history shows multiple workflow-file changes between May and July 2026.
- Latest recorded workflow-file change:
  - 827a4a0, 31 July 2026, Update backup and deployment paths in workflow - Deploy
- Interpretation: older backend runs may represent different workflow versions.
- For backend analysis, runs after commit 827a4a0 should be considered first as a candidate stable period.

### Backend Stable-Workflow Period

Latest recorded workflow-file change:
- Commit: 827a4a054a3270a2c7d697279fd03f9413585ffa
- Time: 31 July 2026 23:53:12 +03:00
- Commit message: Update backup and deployment paths in workflow - Deploy

Candidate stable-period filter:
- workflow = deploy_server.yml
- branch = main
- event = push
- status = completed
- run created at or after 2026-07-31T20:53:12Z

Result:
- 12 completed push/main workflow runs

Interpretation:
The backend has 134 total historical runs, but only 12 runs currently belong to the candidate period after the latest recorded workflow-file change. These 12 still need job-level inspection before they can be considered comparable full build-and-deploy runs.

### Backend Stable-Period Job Breakdown

For the 12 completed push/main runs after the latest workflow-file change:

- 7: check-commit-message = success, build-and-deploy = success
- 5: check-commit-message = success, build-and-deploy = skipped

Interpretation:
Only 7 of the 12 runs executed the full build-and-deploy job.
The 5 skipped runs should not be compared directly with full deployment runs for execution-time analysis.

Current comparable-history summary:
- Frontend: 33 full build-and-deploy runs
- Backend stable period: 7 full build-and-deploy runs

This makes the frontend stronger in terms of directly comparable historical execution data.
