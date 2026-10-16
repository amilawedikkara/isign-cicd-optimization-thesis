# Internship Work vs Thesis Work

## Work Completed Before the Thesis

The iSign Attendance Management System already existed before the thesis. During the practical training/internship, development work included areas such as:

- Android attendance and verification functionality
- Node.js/Express backend functionality and API integration
- parts of the Python/FastAPI verification service
- REST API design and documentation
- frontend Git integration and coordination
- application testing and regression testing
- existing GitHub Actions deployment workflows

These activities form part of the existing system and project background. They are not presented as new thesis contributions.

## New Thesis Work

The thesis contribution starts from the existing iSign system and focuses specifically on CI/CD analysis and optimization. New thesis work includes:

- selecting and documenting one iSign GitHub Actions workflow for detailed study
- defining a measurable CI/CD baseline
- collecting workflow-run and job-level GitHub Actions data
- cleaning and preprocessing the collected data
- performing descriptive statistical analysis
- developing a Python-based CI/CD analysis tool
- using Isolation Forest for anomaly detection
- comparing Isolation Forest findings with a simple statistical baseline method
- investigating detected unusual behaviour using workflow configuration and logs
- identifying one evidence-based CI/CD improvement opportunity
- implementing one justified optimization in the selected iSign workflow
- measuring the workflow before and after the optimization
- evaluating the measured effect and documenting conclusions and recommendations

## Selected Thesis Workflow

Repository: i3cubes/iSign_v3_FE
Workflow: Deploy to Dev Apache Server
Workflow file: .github/workflows/Deploy-to_Dev_Server.yml

The historical workflow configuration and previous workflow runs are treated as existing evidence and baseline material. Changes made specifically as part of the thesis analysis and optimization will be documented separately as thesis contributions.
