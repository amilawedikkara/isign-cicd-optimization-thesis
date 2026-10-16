# Selected iSign Workflow

Selection date: 16 October 2026

## Selected Workflow

Repository: i3cubes/iSign_v3_FE
Workflow: Deploy to Dev Apache Server
Workflow file: .github/workflows/Deploy-to_Dev_Server.yml
Primary branch: development
Trigger: push to development, plus manual workflow_dispatch support

## Reason for Selection

- The frontend has 55 historical workflow runs.
- 33 runs executed the complete build-and-deploy job successfully.
- All 55 historical runs use the push event on the development branch.
- Git history shows the workflow file has remained structurally stable since its introduction in the available local history.
- The backend has more total historical runs, but only 12 runs occur after its latest recorded workflow-file change, and only 7 of those executed the complete build-and-deploy job successfully.
- Therefore, the frontend provides the stronger set of directly comparable historical executions for baseline and anomaly analysis.

## Current Workflow Characteristics

- Node.js 20
- GitHub-hosted ubuntu-latest runner
- npm dependency caching through actions/setup-node
- npm install
- Vite production build using npm run build
- deployment through SCP and SSH
- deployed index.html verification
- commit message must contain the case-sensitive word Deploy before build-and-deploy executes

## Current Quality-Check Findings

- Vitest automated tests exist in package.json.
- The current GitHub Actions workflow does not execute the Vitest tests.
- The workflow calls npm run lint, but the frontend package.json currently has no lint script.
- The lint step uses continue-on-error, so its failure does not stop deployment.

## Scope Note

The selected workflow includes an actual deployment stage, so CI/CD remains an appropriate term for the thesis scope.

No optimization has been selected yet. Optimization decisions will be based on measured workflow data and analysis results.
