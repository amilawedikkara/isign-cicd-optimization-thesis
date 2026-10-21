# 1 INTRODUCTION

## Writing plan

Paragraph 1 - Background

- Explain what CI/CD is.
- Explain why automated CI/CD pipelines are important in software development.
- Mention fast feedback, repeatability and reliable delivery.
- Academic/technical sources are needed here.

Paragraph 2 - iSign context

- Introduce the iSign attendance management system.
- Explain that GitHub Actions workflows already existed before the thesis.
- State that this thesis studies an existing workflow rather than creating CI/CD from zero.

Paragraph 3 - Problem

- iSign may contain unusual or inefficient CI/CD behaviour.
- There was no systematic data-based method being used to identify and evaluate it.
- Manual inspection alone is not enough for consistent historical analysis.

Paragraph 4 - Purpose and objective

- Analyze the selected iSign workflow.
- Develop a Python-based analysis approach.
- Use descriptive statistics and a simple statistical anomaly baseline.
- Use Isolation Forest as an additional anomaly-detection technique.
- Compare the methods.

Paragraph 5 - Development task

- Investigate the findings.
- Select one optimization based on evidence.
- Implement it.
- Compare before and after measurements.
- Do not assume the optimization in advance.

Paragraph 6 - Scope

- Selected frontend GitHub Actions workflow.
- Technical CI/CD execution data only.
- No attendance, employee or user data.
- FastAPI public data only as supporting reference data if needed.

Paragraph 7 - Previous work vs thesis contribution

- Existing iSign system and workflows are starting conditions.
- Separate internship work from new thesis work.
- New thesis work: data collection, preprocessing, analysis, ML comparison, optimization and evaluation.

Paragraph 8 - Research questions
RQ1. What inefficient or unusual behaviour can be identified in the selected iSign frontend GitHub Actions workflow?

RQ2. How does Isolation Forest support the identification of unusual workflow behaviour compared with a simple statistical baseline method?

RQ3. What measurable effect does one evidence-based CI/CD optimization have on the selected iSign workflow?
