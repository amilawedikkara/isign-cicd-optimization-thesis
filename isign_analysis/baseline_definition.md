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
