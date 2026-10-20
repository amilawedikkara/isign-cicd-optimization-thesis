# Thesis Report Outline

## Thesis Title

AI-Assisted CI/CD Pipeline Optimization for an Attendance Management System: A Case Study of iSign


# Front Matter

- Cover page
- Abstract
- Contents
- Glossary, if needed


# 1 INTRODUCTION

The introduction will present:

- background of the thesis
- iSign project context
- problem addressed
- purpose of the thesis
- objectives
- scope
- research questions
- significance of the work

Research questions:

RQ1. What inefficient or unusual behaviour can be identified in the selected iSign frontend GitHub Actions workflow?

RQ2. How does Isolation Forest support the identification of unusual workflow behaviour compared with a simple statistical baseline method?

RQ3. What measurable effect does one evidence-based CI/CD optimization have on the selected iSign workflow?


# 2 KNOWLEDGE BASE

## 2.1 Continuous Integration and Continuous Delivery

Topics:

- Continuous Integration
- Continuous Delivery
- CI/CD pipelines
- automated build and deployment
- fast feedback
- reliability of CI/CD processes


## 2.2 GitHub Actions

Topics:

- workflows
- events and triggers
- jobs
- steps
- runners
- workflow execution
- GitHub Actions data and API


## 2.3 CI/CD Performance Measurement

Topics:

- workflow execution time
- job execution time
- step execution time
- pipeline variability
- failure and rerun information
- resource-use proxies
- importance of comparable measurements


## 2.4 Statistical Analysis of CI/CD Execution Data

Topics:

- descriptive statistics
- mean
- median
- standard deviation
- quartiles
- interquartile range
- statistical outlier detection
- IQR method


## 2.5 Anomaly Detection

Topics:

- anomaly detection concept
- normal and unusual observations
- anomalies versus inefficiencies
- anomaly detection in operational and software-engineering data


## 2.6 Unsupervised Machine Learning

Topics:

- supervised versus unsupervised learning
- unlabeled datasets
- suitability for historical CI/CD data


## 2.7 Isolation Forest

Topics:

- principle of Isolation Forest
- isolation of unusual observations
- anomaly scores
- contamination parameter
- advantages
- limitations
- reason for selecting Isolation Forest


# 3 ISIGN STARTING SITUATION

## 3.1 iSign Attendance Management System

Topics:

- system context relevant to the thesis
- development environment
- role of GitHub repositories
- CI/CD role in the project


## 3.2 Existing iSign CI/CD Workflows

Topics:

- frontend workflow
- backend workflow
- workflow comparison
- available historical data
- workflow stability


## 3.3 Selected Frontend Workflow

Selected repository:

i3cubes/iSign_v3_FE

Selected workflow:

Deploy to Dev Apache Server

Workflow file:

.github/workflows/Deploy-to_Dev_Server.yml

Branch:

development

Topics:

- trigger
- check-commit-message job
- build-and-deploy job
- dependency installation
- build
- SCP transfer
- server synchronization
- deployment verification


## 3.4 Workflow Selection

Topics:

- 55 historical frontend workflow runs
- 33 comparable successful full runs
- backend comparison
- reason for selecting frontend


## 3.5 Existing Quality Checks

Topics:

- available Vitest tests
- tests not currently executed by the selected GitHub Actions workflow
- npm run lint workflow step
- missing frontend lint script
- continue-on-error behaviour


## 3.6 Previous Work and Thesis Contribution

Topics:

- work completed before the thesis
- practical-training contribution
- existing CI/CD implementation
- new work completed specifically during the thesis
- boundary between existing system and thesis development


# 4 DATA AND METHODS

## 4.1 Research Approach

Methods:

- Case Study Approach
- Quantitative Measurement
- Qualitative Analysis
- Agile/Iterative Development


## 4.2 Data Source

Topics:

- GitHub Actions
- GitHub API
- GitHub CLI
- workflow runs
- jobs
- steps
- timestamps


## 4.3 Data Collection

Topics:

- Python data collector
- run-level fields
- job-level fields
- step-level fields
- CSV data storage
- reproducibility


## 4.4 Comparable Run Selection

Topics:

- development branch
- push event
- successful check-commit-message job
- successful full build-and-deploy job
- skipped runs
- failed runs
- cancelled runs
- inclusion and exclusion criteria


## 4.5 Data Preprocessing

Topics:

- timestamps
- missing values
- reruns
- run_attempt
- created_at
- run_started_at
- updated_at
- duration calculations


## 4.6 Descriptive Statistical Analysis

Metrics:

- mean
- median
- standard deviation
- minimum
- maximum
- Q1
- Q3
- IQR


## 4.7 Statistical Anomaly Baseline

Method:

Upper IQR threshold = Q3 + 1.5 × IQR

Topics:

- reason for using a simple baseline
- candidate slow-duration anomalies
- interpretation limitations


## 4.8 Isolation Forest Analysis

Topics:

- selected features
- preprocessing
- model configuration
- random state
- contamination
- anomaly score
- anomaly label
- reproducibility


## 4.9 Comparison of Analysis Methods

Compare:

- IQR statistical baseline
- Isolation Forest

Investigate:

- observations flagged by both
- observations flagged only by IQR
- observations flagged only by Isolation Forest
- technical interpretation


## 4.10 Optimization Evaluation Method

Topics:

- evidence-based optimization selection
- before-and-after design
- comparable workflow executions
- timing metrics
- variability
- resource-use proxy
- tests
- build success
- workflow success
- deployment success


# 5 ANALYSIS AND RESULTS

## 5.1 Baseline Workflow Measurements

Current verified baseline:

- 33 comparable successful runs
- 495 step observations
- workflow median = 70 seconds
- build-and-deploy median = 58 seconds
- SCP median = 19 seconds


## 5.2 Step-Level Performance

Topics:

- recurring workflow-step durations
- longest recurring individual step
- SCP transfer observations


## 5.3 Statistical Anomaly Results

Current IQR thresholds:

- workflow duration > 86.5 seconds
- build-and-deploy duration > 74.5 seconds
- SCP transfer duration > 23 seconds

Current statistically flagged runs:

- Run 52
- Run 19
- Run 37
- Run 55
- Run 38

Current observation:

All five statistically flagged runs contain an SCP transfer duration above the calculated IQR threshold.

This is treated as an investigation target, not yet as proof of an inefficiency.


## 5.4 Isolation Forest Results

To be completed after Isolation Forest analysis.


## 5.5 Statistical Baseline versus Isolation Forest

To be completed after both methods have been executed.


## 5.6 Investigation of Unusual Workflow Behaviour

To be completed after inspection of flagged runs and workflow evidence.


## 5.7 Identified CI/CD Improvement Opportunity

To be completed after anomaly investigation.


# 6 CI/CD OPTIMIZATION AND EVALUATION

## 6.1 Selected Optimization

To be determined from measured evidence.


## 6.2 Optimization Design

To be completed after optimization selection.


## 6.3 Implementation

To document:

- exact workflow change
- affected files
- technical reasoning
- Git commit
- build verification
- test verification
- deployment verification


## 6.4 Post-Optimization Measurements

To be completed after implementation.


## 6.5 Before-and-After Comparison

Compare:

- workflow duration
- job duration
- affected step duration
- variability
- resource-use proxy
- tests
- build
- workflow reliability
- deployment


## 6.6 Effect of the Optimization

This section will answer RQ3 using measured results.


# 7 DISCUSSION

Topics:

- summary of key findings
- answers to RQ1, RQ2 and RQ3
- usefulness of the statistical method
- usefulness of Isolation Forest
- practical value of the optimization
- limitations
- threats to validity
- GitHub-hosted runner variability
- dataset size
- absence of labelled anomaly ground truth
- applicability of the results
- recommendations for future iSign CI/CD development
- possible future research


# REFERENCES

Use OAMK reference guidelines.

Maintain source notes during the thesis work.


# APPENDICES

Possible appendices:

- additional statistical tables
- selected code extracts
- workflow configuration extracts
- supplementary measurements
- analysis-tool documentation