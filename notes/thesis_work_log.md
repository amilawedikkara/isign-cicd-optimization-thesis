
## 16 October 2026 - Week 1 Workflow Selection and Baseline

Completed:
- compared iSign frontend and backend GitHub Actions workflows
- verified frontend: 55 historical runs, including 33 successful full build-and-deploy runs
- verified backend current stable period: 12 runs, including 7 successful full build-and-deploy runs
- selected the frontend Deploy-to_Dev_Server.yml workflow as the primary thesis workflow
- documented the workflow selection and reasoning
- verified frontend and backend package.json scripts
- identified that frontend Vitest tests exist but are not executed by the current workflow
- identified that the frontend workflow calls npm run lint although no frontend lint script currently exists
- finalized three research questions
- documented the boundary between previous internship work and new thesis work
- recorded the frontend baseline repository state and exact commit

Selected frontend baseline commit: 68de2cc81b62b00204d9aade6c0634de32194af6

Next phase: define the data fields and begin reproducible GitHub Actions data collection for the selected frontend workflow.
