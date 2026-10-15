# AI-Assisted CI/CD Pipeline Optimization for iSign

**Bachelor's Thesis | Information Technology | OAMK**

This repository contains my bachelor's thesis development work on analyzing and improving the GitHub Actions CI/CD pipeline of the iSign Attendance Management System.

## Project Goal

Develop and evaluate a Python-based analysis tool for identifying unusual CI/CD pipeline behavior and potential inefficiencies, then implement and measure one evidence-based workflow optimization.

## Thesis Contribution

- analyze one selected iSign GitHub Actions workflow
- collect and preprocess workflow-run and job-level data
- establish measurable pipeline baselines
- compare a simple statistical baseline with Isolation Forest
- investigate anomalies using workflow configuration and logs
- identify and implement one justified CI/CD optimization
- perform controlled before/after measurements
- document results, limitations, and recommendations

Existing iSign application code and previous internship work are treated as the starting system, not as new thesis contributions.

## Technologies

Python, Pandas, Scikit-learn, Isolation Forest, GitHub Actions, GitHub API, GitHub CLI, Git, statistical analysis.

## Current Status

Work in progress - Bachelor's Thesis, 2026.

Completed:
- thesis scope and implementation structure defined
- FastAPI public GitHub Actions dataset feasibility check completed
- 316 structurally comparable FastAPI workflow runs identified as a candidate reference dataset
- thesis analysis workspace and Git repository established

Current work:
- select and document one primary iSign GitHub Actions workflow
- establish the iSign baseline
- inspect available historical workflow data

## Repository Structure

- `plan/` - scope, research questions and schedule
- `notes/` - work log, literature notes and decisions
- `isign_analysis/` - workflow selection, baseline and data availability
- `scripts/` - data collection and analysis implementation
- `data/` - public, processed and sample datasets
- `results/` - measurements, tables and figures
- `report/` - thesis report working material
- `references/` - source and literature notes

## Confidentiality

Only sanitized technical evidence and non-confidential results are intended for this repository. Credentials, employee data, attendance records, raw confidential logs, and restricted company material are excluded.
