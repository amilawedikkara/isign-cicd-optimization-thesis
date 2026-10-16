# iSign GitHub Actions Workflow Inventory



Date inspected: 15 October 2026



Purpose:

Compare the existing frontend and backend GitHub Actions workflows before selecting ONE workflow as the main thesis case.



---



## 1. Backend Workflow



Repository:

iSign_v3_BE



Workflow file:

.github/workflows/deploy_server.yml



Workflow name:

Deploy to Apache Server



Trigger:

- push to main

- workflow_dispatch



Jobs:

1. check-commit-message

2. build-and-deploy



Dependency:

- build-and-deploy depends on check-commit-message



Deployment condition:

- deployment only runs when the commit message contains "deploy"

- backend converts the commit message to lowercase before checking



Runner:

- ubuntu-latest



Node.js:

- version 20



Caching:

- npm cache enabled through actions/setup-node



Main build/deployment steps:

- checkout repository

- setup Node.js

- npm install

- npm run lint

- npm run build

- create server backup

- prepare temporary deployment directory

- transfer dist, node_modules and package.json using SCP

- synchronize deployed files

- verify deployed server.js

- restart backend service

- success/failure notification



Tests:

- no test command is present in this workflow



Deployment:

- yes



Possible timing points:

- check-commit-message

- dependency installation

- lint

- build

- backup creation

- SCP transfer

- deployment synchronization

- deployment verification



Notes:

- actual deployment is included

- npm caching is already enabled

- node_modules is transferred to the server

- the workflow step is named "Build React app" even though this is the backend repository; package.json should be inspected before interpreting this further



---



## 2. Frontend Workflow



Repository:

iSign_v3_FE



Workflow file:

.github/workflows/Deploy-to_Dev_Server.yml



Workflow name:

Deploy to Dev Apache Server



Trigger:

- push to development

- workflow_dispatch



Jobs:

1. check-commit-message

2. build-and-deploy



Dependency:

- build-and-deploy depends on check-commit-message



Deployment condition:

- deployment only runs when the commit message contains "Deploy"

- the frontend check is case-sensitive



Runner:

- ubuntu-latest



Node.js:

- version 20



Caching:

- npm cache enabled through actions/setup-node



Main build/deployment steps:

- checkout repository

- setup Node.js

- npm install

- npm run lint

- npm run build

- transfer dist files using SCP

- synchronize deployed files

- verify deployed index.html

- success/failure notification



Tests:

- no test command is present in this workflow



Deployment:

- yes



Possible timing points:

- check-commit-message

- dependency installation

- lint

- build

- SCP transfer

- deployment synchronization

- deployment verification



Notes:

- actual deployment is included

- npm caching is already enabled

- deployment targets the development frontend server

- only dist build output is transferred

- no explicit automated test command is present



---



## Initial Comparison



Both workflows:

- use GitHub Actions

- use ubuntu-latest

- use Node.js 20

- use npm caching

- run npm install

- run ESLint

- run npm run build

- deploy through SSH/SCP

- have no explicit automated test command

- use a commit-message condition before deployment



Important differences:

- Backend runs on main

- Frontend runs on development

- Backend checks "deploy" case-insensitively

- Frontend checks "Deploy" case-sensitively

- Backend deployment includes backup creation and backend service restart

- Frontend mainly transfers built dist files and verifies index.html



Decision:

Not selected yet.



Next:

Compare historical run availability, workflow stability, comparable job execution, and optimization opportunities before choosing the thesis workflow.


## Package Script Verification

### Frontend

package.json scripts:
- dev = vite
- build = vite build
- preview = vite preview
- test = vitest
- test:ui = vitest --ui
- test:run = vitest run

Findings:
- npm run build performs a Vite production build.
- Automated Vitest tests exist.
- The GitHub Actions workflow does not execute the tests.
- The workflow executes npm run lint, but no lint script exists in the frontend package.json.
- The lint step uses continue-on-error, so failure of that step does not stop deployment.

### Backend

package.json scripts:
- dev = ts-node-dev --respawn src/server.ts
- build = tsc
- start = node dist/server.js
- lint = tsc --noEmit
- test = vitest run
- test:coverage = vitest run --coverage

Findings:
- npm run build compiles the backend using TypeScript.
- Automated Vitest tests and coverage are available.
- The GitHub Actions workflow does not execute the tests.
- The workflow step named Run ESLint actually runs tsc --noEmit, not ESLint.
- The workflow step named Build React app actually runs the backend TypeScript build.
