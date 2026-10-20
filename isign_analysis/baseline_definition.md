# iSign Frontend Baseline Definition

Baseline recorded: 16 October 2026

## Repository State

Repository: i3cubes/iSign_v3_FE
Branch: development
Commit: 68de2cc81b62b00204d9aade6c0634de32194af6
Commit time: 31 August 2026 08:57:44 +03:00
Commit message: Merge pull request #49 from i3cubes/integration/report-ui
Remote status: local development branch matches origin/development

Local note: an untracked coverage/ directory exists. It is not part of the committed repository state and is treated as a local generated artifact.

## Selected Workflow

Workflow: Deploy to Dev Apache Server
Workflow file: .github/workflows/Deploy-to_Dev_Server.yml
Trigger branch: development
Runner: ubuntu-latest
Node.js version: 20

## Historical Baseline Data

Total historical workflow runs: 55
Full successful build-and-deploy runs: 33
Runs where build-and-deploy was skipped: 22

The workflow file appears structurally stable across the available local Git history.

## Current Workflow Behaviour

The workflow:
- checks the commit message for the case-sensitive word Deploy
- uses npm dependency caching through actions/setup-node
- runs npm install
- calls npm run lint
- runs npm run build
- deploys the built frontend through SCP and SSH
- verifies the deployed index.html

## Current Quality Findings

- npm run build executes vite build
- Vitest tests exist in package.json
- the GitHub Actions workflow does not currently run the Vitest tests
- the workflow calls npm run lint, but package.json has no lint script
- the lint step uses continue-on-error, so failure does not stop deployment

## Baseline Purpose

This baseline represents the selected iSign frontend CI/CD workflow before any thesis-specific optimization is implemented. Historical execution-time and job-level measurements will be added after data collection and preprocessing.

No optimization has been selected or applied yet.

## Measured Historical Baseline

Comparable successful full workflow runs analyzed: 33

Run-level duration statistics:
- workflow duration: mean 70.55 s, median 70.0 s, standard deviation 8.96 s, range 57-90 s
- check-commit-message duration: mean 5.27 s, median 6.0 s, standard deviation 1.38 s, range 3-8 s
- build-and-deploy duration: mean 57.88 s, median 58.0 s, standard deviation 7.56 s, range 45-77 s

Step-level finding:
- Transfer build files via SCP is the longest recurring individual step.
- SCP transfer duration: mean 20.64 s, median 19.0 s, standard deviation 4.72 s, range 17-40 s.

## Rerun Handling

Workflow execution duration is calculated using run_started_at to updated_at.
The original created_at timestamp is not used for execution duration because reruns may keep the original workflow creation time and would otherwise produce misleadingly long durations.

Example:
- Run 1, attempt 2 initially appeared as 1661 s when calculated from created_at.
- Using run_started_at, the same attempt was approximately 57 s.
- Therefore reruns must be handled consistently during preprocessing.
