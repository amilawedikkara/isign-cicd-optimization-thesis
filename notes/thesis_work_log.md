## 16 October 2026 - Week 1 Workflow Selection and Baseline

### Completed

- compared iSign frontend and backend GitHub Actions workflows
- verified frontend: 55 historical runs, including 33 successful full build-and-deploy runs
- verified backend current stable period: 12 runs, including 7 successful full build-and-deploy runs
- selected the frontend `Deploy-to_Dev_Server.yml` workflow as the primary thesis workflow
- documented the workflow selection and reasoning
- verified frontend and backend `package.json` scripts
- identified that frontend Vitest tests exist but are not executed by the current workflow
- identified that the frontend workflow calls `npm run lint` although no frontend lint script currently exists
- finalized three research questions
- documented the boundary between previous internship work and new thesis work
- recorded the frontend baseline repository state and exact commit

Selected frontend baseline commit:

`68de2cc81b62b00204d9aade6c0634de32194af6`

### Next

- define the data fields
- begin reproducible GitHub Actions data collection for the selected frontend workflow


## 21 October 2026 - Statistical Baseline and Literature Foundation

### Completed

- completed reproducible GitHub Actions data collection
- collected 55 historical frontend workflow runs
- selected 33 comparable successful full build-and-deploy runs
- collected 495 comparable step observations
- corrected the workflow-duration calculation for reruns by using `run_started_at -> updated_at`
- completed workflow-, job-, and step-level descriptive statistics
- calculated mean, median, standard deviation, minimum, maximum, Q1, Q3, and IQR
- completed the IQR-based statistical anomaly baseline
- calculated the following IQR upper thresholds:
  - workflow duration > 86.5 seconds
  - `build-and-deploy` duration > 74.5 seconds
  - SCP transfer duration > 23 seconds
- identified 5 of 33 runs for further investigation
- identified 3 workflow-duration anomalies
- identified 2 `build-and-deploy` duration anomalies
- identified 5 SCP-duration anomalies
- observed that SCP duration was above its IQR threshold in all five flagged runs
- recorded SCP as a recurring investigation candidate, not yet a confirmed inefficiency
- completed focused literature review notes S001-S014
- covered CI/CD, Continuous Delivery, GitHub Actions, CI performance, anomaly detection, Isolation Forest, IQR, unsupervised anomaly evaluation, and experimental evaluation
- recorded literature notes in `references/source_notes.md`
- kept S015 pending until the actual evidence-based CI/CD optimization is selected
- continued thesis report preparation in parallel

### Current Interpretation

The statistical baseline is now ready for later comparison with Isolation Forest.

The SCP deployment-transfer step appears repeatedly in the statistically unusual runs, but this does not yet prove that SCP is the workflow bottleneck or that it should be optimized.

Further analysis with Isolation Forest and technical investigation is required before selecting the optimization.

### Next

- finalize preprocessing rules
- verify missing-value handling
- select final numerical features
- prepare the Isolation Forest input dataset
- implement and run Isolation Forest
- compare Isolation Forest results with the IQR baseline
- investigate the flagged workflow runs and steps
- continue report writing in parallel:
  - Introduction
  - Knowledge Base
  - iSign Starting Situation
  - Data and Methods