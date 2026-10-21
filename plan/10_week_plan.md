# 10-Week Thesis Plan

## Thesis

**Title:**  
AI-Assisted CI/CD Pipeline Optimization for an Attendance Management System: A Case Study of iSign

**Primary case:**  
iSign Attendance Management System

**Selected repository:**  
i3cubes/iSign_v3_FE

**Selected workflow:**  
Deploy to Dev Apache Server

**Workflow file:**  
.github/workflows/Deploy-to_Dev_Server.yml

**Primary branch:**  
development

# Overall Work Structure

The thesis work is divided into two parallel streams:

1. **Technical / Research Work**
   - CI/CD data collection
   - preprocessing
   - statistical analysis
   - Isolation Forest
   - anomaly investigation
   - optimization
   - before/after evaluation

2. **Literature Review & Report Writing**
   - knowledge base
   - research methods
   - implementation documentation
   - results
   - discussion
   - conclusions

Writing and literature review will continue throughout the project instead of being postponed until the final week.

# Week 1 - 15-21 October 2026

## Technical / Research Work

### Focus

Select and understand one iSign CI/CD workflow.

### Tasks

- inspect frontend GitHub Actions workflow
- inspect backend GitHub Actions workflow
- compare available historical workflow data
- compare workflow-version stability
- compare comparable full workflow runs
- select one primary iSign workflow
- record repository and branch
- record selected workflow file
- record baseline commit
- inspect workflow triggers
- inspect jobs
- inspect job dependencies
- inspect individual steps
- inspect build commands
- inspect deployment process
- inspect available automated tests
- inspect existing quality checks
- finalize thesis scope
- finalize research questions
- document internship work versus thesis work
- define initial CI/CD baseline

### Result

Selected repository:

i3cubes/iSign_v3_FE

Selected workflow:

Deploy to Dev Apache Server

Historical frontend runs:

55

Comparable successful full build-and-deploy runs:

33

Backend comparison:

- 134 total historical backend runs
- 12 runs after the latest workflow-file change
- 7 successful full build-and-deploy runs in the stable backend period

The frontend was selected because it provides a stronger set of structurally comparable historical workflow executions.

## Literature & Report Writing

### Introduction

Start writing:

- thesis background
- problem addressed
- purpose
- objectives
- scope
- research questions
- commissioner/project context

### Initial Literature Review

Start notes on:

- DevOps
- Continuous Integration
- Continuous Delivery
- CI/CD pipelines
- GitHub Actions
- fast feedback in CI/CD

## Status

**COMPLETED**

# Week 2 - 22-28 October 2026

## Technical / Research Work

### Focus

Collect, preprocess, and statistically analyze the selected iSign frontend workflow.

### Data Collection

Completed:

- defined run-level fields
- defined job-level fields
- defined step-level fields
- developed a reproducible Python GitHub Actions collector
- retrieved workflow-run data using the GitHub API
- retrieved job-level information
- retrieved step-level information
- saved raw data as structured CSV files

### Comparable Run Selection

Completed:

- used push runs from the `development` branch
- inspected the `check-commit-message` job
- inspected the `build-and-deploy` job
- separated skipped `build-and-deploy` runs
- retained successful full `build-and-deploy` runs for performance analysis
- documented inclusion and exclusion rules

### Preprocessing

Completed so far:

- inspected timestamps
- inspected skipped steps
- inspected cancelled jobs
- inspected failed jobs
- inspected reruns
- used `run_attempt` consistently
- distinguished `created_at` from `run_started_at`
- calculated execution durations consistently
- verified the comparable workflow structure

Still to finalize:

- confirm missing-value handling
- confirm final preprocessing rules
- confirm the numerical features to be used for Isolation Forest
- create the final Isolation Forest input dataset

### Rerun Rule

Workflow execution duration is calculated using:

`run_started_at -> updated_at`

Do not use:

`created_at -> updated_at`

for rerun execution duration because `created_at` may represent the original workflow attempt rather than the actual start time of the rerun.

### Current Dataset

Historical frontend workflow runs:

55

Comparable successful full runs:

33

Step observations:

495

Calculation:

33 runs × 15 steps = 495 step observations

### Descriptive Statistics

Completed calculations:

- mean
- median
- standard deviation
- minimum
- maximum
- Q1
- Q3
- IQR

Analyzed:

- workflow duration
- `check-commit-message` duration
- `build-and-deploy` duration
- important individual step durations

### Current Workflow Baseline

Workflow duration:

- mean = 70.55 seconds
- median = 70.0 seconds
- standard deviation = 8.96 seconds
- range = 57-90 seconds

`check-commit-message`:

- mean = 5.27 seconds
- median = 6.0 seconds
- standard deviation = 1.38 seconds
- range = 3-8 seconds

`build-and-deploy`:

- mean = 57.88 seconds
- median = 58.0 seconds
- standard deviation = 7.56 seconds
- range = 45-77 seconds

### Step-Level Baseline

Longest recurring individual step:

`Transfer build files via SCP`

SCP duration:

- mean = 20.64 seconds
- median = 19.0 seconds
- standard deviation = 4.72 seconds
- range = 17-40 seconds

### Distribution Analysis

Workflow duration:

- Q1 = 64 seconds
- median = 70 seconds
- Q3 = 73 seconds
- IQR = 9 seconds

`build-and-deploy`:

- Q1 = 52 seconds
- median = 58 seconds
- Q3 = 61 seconds
- IQR = 9 seconds

SCP transfer:

- Q1 = 18 seconds
- median = 19 seconds
- Q3 = 20 seconds
- IQR = 2 seconds

### Statistical Anomaly Baseline

A simple statistical method was applied before Isolation Forest.

Method:

IQR upper threshold

Formula:

`Upper threshold = Q3 + 1.5 × IQR`

Calculated upper thresholds:

- workflow duration > 86.5 seconds
- `build-and-deploy` duration > 74.5 seconds
- SCP transfer duration > 23 seconds

### IQR Anomaly Results

The IQR baseline identified 5 of the 33 comparable workflow runs for further investigation.

Results:

- 3 runs exceeded the workflow-duration threshold
- 2 runs exceeded the `build-and-deploy` threshold
- 5 runs exceeded the SCP-duration threshold

SCP duration was above its IQR threshold in all five flagged runs.

This does not yet prove that SCP is an inefficient part of the workflow.

Current interpretation:

SCP is a recurring candidate for technical investigation.

The anomaly results will later be compared with Isolation Forest before deciding whether SCP or another workflow component represents a real optimization opportunity.

### Quality Baseline

Recorded and inspected:

- npm build command
- available test commands
- build behaviour
- workflow result
- deployment process
- current GitHub Actions quality checks

Existing findings:

- Vitest automated tests exist
- the current GitHub Actions workflow does not execute Vitest
- the workflow calls `npm run lint`
- the frontend `package.json` does not currently contain a lint script
- the lint step uses `continue-on-error`
- a lint failure therefore does not stop deployment

## Literature & Report Writing

### Literature Review

Focused literature review completed for sources S001-S014.

Topics covered:

- Continuous Integration
- Continuous Delivery
- CI/CD pipelines
- fast feedback
- GitHub Actions workflow structure
- GitHub REST API data collection
- CI build duration and performance
- anomaly detection
- unsupervised anomaly detection
- Isolation Forest
- scikit-learn Isolation Forest implementation
- statistical outlier detection
- IQR
- evaluation of unsupervised anomaly detection
- experimental design
- before/after performance evaluation

Literature notes are recorded in:

`references/source_notes.md`

S015 is intentionally pending.

It will be selected after the technical analysis identifies the actual evidence-based CI/CD optimization so that the literature supports the selected optimization rather than determining the optimization in advance.

### iSign Starting Situation

Report-writing topics:

- iSign system background
- CI/CD starting situation
- selected frontend repository
- selected workflow
- workflow structure
- workflow trigger
- workflow jobs
- workflow steps
- reason for selecting the frontend instead of the backend
- current quality-check findings

### Data Source

Report-writing topics:

- GitHub Actions as the technical data source
- GitHub REST API
- workflow-run data
- job-level data
- step-level data
- timestamp-based duration calculation
- comparable-run selection

### Baseline Method

Report-writing topics:

- why a baseline is needed
- descriptive statistics
- mean
- median
- standard deviation
- quartiles
- IQR
- IQR upper threshold
- interpretation of candidate statistical anomalies

### Report Writing Status

Report writing continues in parallel with the technical work.

Immediate writing areas:

- Introduction
- Knowledge Base
- iSign Starting Situation
- Data and Methods

The statistical baseline and literature review now provide material that can be used when drafting these sections.

## Completed by 21 October 2026

- completed reproducible GitHub Actions data collection
- selected 33 comparable successful full workflow runs
- collected 495 comparable step observations
- calculated workflow-, job-, and step-level descriptive statistics
- calculated Q1, Q3, and IQR
- defined and applied the IQR statistical anomaly baseline
- identified 5 of 33 runs for further investigation
- identified SCP duration above the IQR threshold in all 5 flagged runs
- completed focused literature notes S001-S014
- recorded literature in `references/source_notes.md`
- prepared the statistical baseline for later comparison with Isolation Forest

## Still in Progress

- finalize preprocessing rules
- verify final missing-value handling
- select final numerical features for Isolation Forest
- prepare the final Isolation Forest input dataset
- continue thesis report writing in parallel

## Status

**IN PROGRESS**

Work is currently ahead of the original calendar schedule.

# Week 3 - 29 October-4 November 2026

## Technical / Research Work

### Focus

Finalize preprocessing and prepare the ML/anomaly-detection dataset.

### Tasks

- finalize preprocessing rules
- verify comparable observations
- document inclusion criteria
- document exclusion criteria
- verify missing-value handling
- verify rerun handling
- check duplicated executions
- verify timestamps
- verify calculated durations
- select meaningful numerical features
- create processed iSign analysis dataset

### Feature Selection

Potential features may include:

- workflow duration
- build-and-deploy duration
- check-commit-message duration
- SCP transfer duration
- Vite build duration
- dependency-installation duration
- Node.js setup duration
- other stable comparable steps

Do not use every available field automatically.

Choose features that are:

- comparable
- reliable
- numerical
- technically meaningful
- relevant to the research questions

### FastAPI Reference Dataset

If additional data is needed for ML method development:

Use:

fastapi/fastapi

Workflow:

Test

Candidate comparable runs:

316

Main comparable unit:

15 test-matrix jobs

FastAPI remains supporting reference data.

It does not replace iSign as the thesis case.

## Literature & Report Writing

### Data Collection & Preprocessing

Write:

- GitHub API data collection
- run/job/step structure
- comparable-run selection
- timestamp handling
- rerun handling
- skipped/cancelled job handling
- missing-value handling
- duration calculation
- feature-selection reasoning

### Literature Review

Study:

- anomaly detection
- anomalies in software engineering data
- unsupervised machine learning
- anomaly detection in CI/CD or DevOps
- ML-assisted DevOps
- difference between anomaly and inefficiency

## Expected Outcome

- clean processed iSign dataset
- documented preprocessing method
- selected numerical features
- Isolation-Forest-ready data

# Week 4 - 5-11 November 2026

## Technical / Research Work

### Focus

Implement Isolation Forest and begin comparison with the statistical baseline.

### Tasks

- create Isolation Forest Python implementation
- load processed dataset
- select final feature set
- define random_state
- define contamination strategy
- fit Isolation Forest
- calculate anomaly scores
- generate anomaly labels
- rank unusual workflow runs
- inspect flagged observations
- save results
- start comparing flagged observations with statistical baseline results

### Important Rule

Isolation Forest is an analysis technique.

It is not the overall thesis methodology.

The overall approach remains:

- Case Study Approach
- Quantitative Measurement
- Qualitative Analysis
- Agile/Iterative Development

### Evaluation Limitation

Historical CI/CD data does not contain verified anomaly labels.

Therefore do not claim:

Isolation Forest accuracy = X%

unless true labelled ground truth exists.

Instead evaluate:

- which runs are flagged
- how unusual they are technically
- whether statistical baseline also flags them
- whether the findings help identify investigation targets

## Literature & Report Writing

### Knowledge Base - Isolation Forest

Write:

- anomaly detection concept
- supervised vs unsupervised learning
- why unsupervised learning fits this problem
- Isolation Forest concept
- how Isolation Forest isolates unusual observations
- anomaly score
- contamination parameter
- advantages
- limitations
- why Isolation Forest was selected

### Analysis Methods

Start writing:

- simple statistical baseline
- IQR threshold method
- Isolation Forest method
- input features
- preprocessing requirements
- comparison approach

## Expected Outcome

- first Isolation Forest model
- anomaly scores
- anomaly labels
- first statistical-vs-ML comparison

# Week 5 - 12-18 November 2026

## Technical / Research Work

### Focus

Finish statistical method versus Isolation Forest comparison and investigate flagged runs.

### Tasks

Compare:

Statistical baseline
versus
Isolation Forest

Identify:

- runs flagged by both
- runs flagged only statistically
- runs flagged only by Isolation Forest
- runs considered normal by both

### Investigation

For important anomalies:

- inspect job durations
- inspect step durations
- inspect workflow configuration
- inspect GitHub Actions logs where useful
- inspect repeated patterns
- inspect unusual SCP duration
- inspect build duration
- inspect dependency installation
- inspect deployment behaviour

### Important Distinction

An anomaly is not automatically an inefficiency.

Process:

Anomaly detected
->
technical investigation
->
identify reason
->
determine whether it represents a real inefficiency

### Research Questions

Develop evidence for:

RQ1:
What inefficient or unusual behaviour can be identified in the selected iSign frontend GitHub Actions workflow?

RQ2:
How does Isolation Forest support the identification of unusual workflow behaviour compared with a simple statistical baseline method?

## Literature & Report Writing

### Analysis Methods

Finish writing:

- statistical baseline
- Isolation Forest
- feature selection
- method comparison

### Preliminary Results

Write:

- statistical anomalies
- Isolation Forest anomalies
- overlapping findings
- differences
- recurring slow steps
- preliminary technical interpretation

### Literature Review

Study:

- statistical outlier methods
- IQR outlier detection
- ML anomaly detection
- advantages/disadvantages of simple statistical methods
- advantages/disadvantages of Isolation Forest
- interpretation of anomaly scores

## Expected Outcome

- statistical vs Isolation Forest comparison
- investigated anomalies
- preliminary RQ1 answer
- preliminary RQ2 answer
- candidate real inefficiency

# Week 6 - 19-25 November 2026

## Technical / Research Work

### Focus

Select one evidence-based CI/CD optimization.

### Tasks

Review:

- statistical findings
- Isolation Forest findings
- workflow configuration
- recurring slow steps
- identified technical inefficiencies

Select one practical optimization.

The optimization must be selected because of evidence.

Do not choose an optimization in advance.

Process:

Measure
->
Analyze
->
Identify problem
->
Select optimization

Possible categories:

- deployment-transfer improvement
- dependency-installation improvement
- caching improvement
- unnecessary workflow work
- workflow-step correction
- job restructuring
- parallelization
- another evidence-supported improvement

### Before/After Evaluation Design

Define:

- baseline workflow duration
- baseline variability
- affected job duration
- affected step duration
- build result
- test result
- workflow result
- deployment result
- resource-use proxy where suitable

## Literature & Report Writing

### Identified Inefficiency

Write:

- measured evidence
- why it matters
- technical cause
- relationship to anomaly findings

### Optimization Justification

Write:

- selected optimization
- why it is appropriate
- expected technical effect
- risks
- evaluation metrics

### Literature Review

Study literature specifically related to the chosen optimization.

Examples:

- dependency caching
- deployment optimization
- incremental transfer
- pipeline parallelization
- workflow optimization

## Expected Outcome

- one justified optimization
- before/after measurement plan
- technical literature supporting the decision

# Week 7 - 26 November-2 December 2026

## Technical / Research Work

### Focus

Implement the selected optimization.

### Tasks

- create suitable development branch if required
- implement one isolated CI/CD change
- verify YAML syntax
- verify workflow configuration
- run application build
- run required automated tests
- verify deployment functionality
- document exact files changed
- document exact commit
- keep optimization separate from unrelated code changes

### Quality Rule

Do not improve pipeline speed by simply removing important checks.

Required functionality must remain:

- build
- tests
- workflow success
- deployment

## Literature & Report Writing

### Implementation Chapter

Write:

- original configuration
- identified problem
- selected solution
- exact technical change
- implementation reasoning
- files modified
- workflow changes
- build verification
- test verification
- deployment verification

## Expected Outcome

- optimization implemented
- implementation evidence
- build/test/deployment evidence
- implementation chapter draft

# Week 8 - 3-9 December 2026

## Technical / Research Work

### Focus

Collect post-optimization measurements.

### Tasks

- execute several comparable optimized workflow runs
- collect workflow-level data
- collect job-level data
- collect step-level data
- use the same collector where possible
- use the same duration definitions
- verify rerun handling
- record failures
- record skipped jobs
- record cancelled jobs
- record build results
- record test results
- record workflow results
- record deployment results

### Comparability

Use the same or equivalent:

- branch
- workflow
- build process
- runner environment
- deployment target
- metric definitions

## Literature & Report Writing

### Evaluation Method

Write:

- experiment design
- before/after comparison
- number of runs
- metrics
- controlled conditions
- comparability
- quality checks
- reliability checks
- resource-use proxy

## Expected Outcome

- post-optimization dataset
- evaluation-method chapter draft
- comparable before/after measurements

# Week 9 - 10-16 December 2026

## Technical / Research Work

### Focus

Evaluate before versus after.

### Tasks

Compare:

Before optimization
versus
After optimization

Evaluate:

- median workflow duration
- mean workflow duration
- variability
- build-and-deploy duration
- affected step duration
- other important step durations
- workflow reliability
- test outcomes
- deployment success
- resource-use proxy

### Important Distinction

Elapsed time and resource use are different.

For example:

Parallelization may reduce elapsed time while keeping total runner execution time similar.

Report them separately if relevant.

### Performance Target

Approximately 20% improvement may be used as a target.

It is not a guaranteed result.

Report the actual measured result.

### Research Question

Answer:

RQ3:
What measurable effect does one evidence-based CI/CD optimization have on the selected iSign workflow?

## Literature & Report Writing

### Results

Write:

- before/after results
- tables
- graphs
- percentage change
- variability
- quality-check results
- RQ3 answer

### Discussion

Start writing:

- interpretation
- limitations
- reliability
- validity
- GitHub runner variability
- small dataset limitations
- ML limitations

## Expected Outcome

- completed evaluation
- RQ3 answered
- results chapter mostly complete
- discussion draft

# Week 10 - 17-23 December 2026

## Technical / Research Work

### Focus

Final checks and reproducibility.

### Tasks

- verify all scripts still run
- verify result files
- verify tables
- verify figures
- review Git history
- review README
- verify no confidential material is published
- verify reproducibility
- final repository cleanup

## Literature & Report Writing

### Complete Discussion

Write:

- interpretation of findings
- comparison of methods
- limitations
- threats to validity
- practical significance

### Conclusions

Answer clearly:

RQ1
RQ2
RQ3

### Recommendations

Write:

- future iSign CI/CD improvements
- future analysis improvements
- possible future ML improvements

### Abstract

Write the abstract after the results are final.

### Final Review

Check:

- references
- citations
- terminology
- figures
- tables
- formatting
- grammar
- confidentiality
- contribution boundaries
- appendices

## Expected Outcome

- complete thesis report
- complete thesis repository
- final reproducible results
- submission-ready work

# Current Position

## Week 1

COMPLETED

## Week 2

IN PROGRESS

Work is currently ahead of the original calendar schedule.

# Current Completed Work

- selected iSign frontend workflow
- compared frontend and backend workflow history
- finalized research questions
- documented internship work versus thesis work
- recorded baseline repository state
- created reproducible GitHub Actions data collector
- collected 55 historical frontend workflow runs
- identified 33 comparable successful full runs
- collected 495 step observations
- calculated workflow-level baseline
- calculated job-level baseline
- calculated step-level baseline
- identified and corrected rerun timestamp issue
- calculated mean, median, standard deviation, minimum, and maximum
- calculated Q1, Q3, and IQR
- defined and applied IQR statistical anomaly thresholds
- identified 5 candidate unusual runs
- identified SCP duration above its IQR threshold in all 5 flagged runs
- identified SCP as a recurring investigation candidate
- completed literature notes S001-S014
- continued thesis report writing and preparation in parallel

# Current Exact Technical Position

33 comparable workflow runs
->
descriptive statistics completed
->
normal behaviour understood
->
IQR statistical anomaly threshold applied
->
5 candidate unusual runs identified
->
SCP identified as a recurring investigation candidate
->
**CURRENT: finalize preprocessing and prepare ML dataset**
->
Isolation Forest
->
compare statistical baseline with Isolation Forest
->
investigate actual inefficiencies
->
select one evidence-based optimization
->
add S015 supporting the selected optimization
->
implement optimization
->
before/after evaluation
