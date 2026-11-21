# Thesis Meeting 5 – Chapter 7 Evaluation Summary and Next Steps

**Thesis title:**\
AI-Assisted CI/CD Pipeline Optimization for an Attendance Management System: A Case Study of iSign

**Main focus of this meeting:**\
Review Chapter 7, confirm the answer to Research Question 3, discuss the diagnostic results, and agree on the next steps for Chapter 8 and the final thesis.

---

## 1. Chapter 7 purpose

Chapter 7 evaluates the Native SCP optimization selected in Chapter 6.

The main research question evaluated in this chapter is:

**RQ3. What measurable effect does one evidence-based CI/CD optimization have on workflow duration and resource use, while maintaining the required build, test, and deployment quality?**

The main comparison is between:

- Docker SCP with Vitest
- Native SCP with Vitest

The same frontend project, Node.js setup, dependencies, Vitest command, React build, development server, deployment target, synchronization, and verification steps were used in both workflows.

The main technical difference was the SCP implementation.

Docker used:

- `appleboy/scp-action`
- Docker-based SCP setup
- SCP transfer

Native used:

- SSH known-host preparation
- remote folder preparation
- native `scp` command

Vitest was included in both workflows as the same quality gate. It was not part of the optimization itself.

---

## 2. Main evaluation dataset

The main Chapter 7 evaluation contains:

- 14 Docker SCP runs
- 14 Native SCP runs
- 28 runs in total
- Vitest enabled in all runs
- all runs completed successfully

Three main performance measures were evaluated:

1. workflow duration
2. resource-use proxy
3. SCP-related duration

The resource-use proxy is the total job execution time. It is only an indirect proxy because direct CPU and memory data were not available.

---

## 3. Main performance results

### Workflow duration

Docker mean: **89.43 seconds**

Native mean: **87.00 seconds**

Difference: **2.43 seconds faster with Native**

Reduction: **2.72%**

Welch p-value: **0.5749**

95% confidence interval: **-11.24 to 6.38 seconds**

The Native mean was lower, but the difference was not statistically significant.

---

### Resource-use proxy

Docker mean: **79.57 seconds**

Native mean: **77.93 seconds**

Difference: **1.64 seconds lower with Native**

Reduction: **2.06%**

Welch p-value: **0.5079**

95% confidence interval: **-6.68 to 3.39 seconds**

The Native mean was again lower, but the difference was not statistically significant.

---

### SCP-related duration

Docker mean: **22.64 seconds**

Native mean: **21.14 seconds**

Difference: **1.50 seconds faster with Native**

Reduction: **6.62%**

Welch p-value: **0.1558**

95% confidence interval: **-3.61 to 0.61 seconds**

Native SCP had a lower mean SCP-related duration, but the difference was not statistically significant in the main 14-by-14 evaluation.

---

## 4. Main statistical conclusion

Native SCP showed lower mean values in all three performance measures:

- workflow duration
- resource-use proxy
- SCP-related duration\
  \
  &#x20;all three p-values were above 0.05.

Therefore, the main Chapter 7 evaluation does not provide enough statistical evidence to claim that Native SCP significantly reduced the performance measures under the tested conditions.

This is an important result.

The thesis should not claim a statistically significant overall improvement based on the main 14-by-14 dataset.

---

## 5. Quality results

The optimization also had to maintain build, test, and deployment quality.

All 28 runs in the main dataset passed:

- Vitest
- frontend production build
- SCP transfer
- file synchronization
- deployment verification
- complete build-and-deploy job

Results:

- Docker: 14/14 successful
- Native: 14/14 successful

Success rate:

**100% for both methods**

Therefore, replacing Docker SCP with Native SCP did not reduce the required build, test, or deployment quality in the main evaluation.

---

## 6. Vitest diagnostic analysis

Vitest was examined separately because it was identical in both workflows and was not part of the SCP optimization.

Mean Vitest time:

Docker: **20.36 seconds**

Native: **20.43 seconds**

Difference: **0.07 seconds**

Welch p-value: **0.9654**

95% confidence interval: **-3.28 to 3.43 seconds**

No statistically significant difference was found.

This means the evaluation did not show evidence that the SCP implementation itself affected the Vitest step.

Observed Vitest timing differences were treated as normal run-to-run variation.

---

## 7. No-Vitest diagnostic analysis

A second diagnostic analysis used seven paired Docker and Native runs without the Vitest step.

These runs were kept separate from the main dataset.

Their purpose was to look more directly at the SCP-related part of the workflow with fewer unrelated timing components.

### Results

Docker mean SCP-related duration: **26.43 seconds**

Native mean SCP-related duration: **21.00 seconds**

Difference: **5.43 seconds faster with Native**

Reduction: **20.54%**

Paired t-test: **t = -3.596**

Paired p-value: **0.0114**

95% confidence interval: **-9.12 to -1.73 seconds**

Pair-level result:

- Native faster in 5 of 7 pairs
- equal in 2 of 7 pairs
- Native slower in 0 of 7 pairs

This diagnostic result was statistically significant.

It gives supporting evidence that Native SCP can reduce the SCP-related duration under the no-Vitest diagnostic conditions.

However, this result must remain separate from the main 14-by-14 Vitest-enabled evaluation.

It does not replace the main RQ3 result.

---

## 8. Important difference between the main result and diagnostic result

The thesis now has two different but compatible findings.

### Main evaluation

14 Docker + 14 Native runs with Vitest:

- Native means were lower
- SCP reduction = 6.62%
- p = 0.1558
- not statistically significant

### Supporting no-Vitest diagnostic

7 paired Docker + 7 paired Native runs:

- Native SCP was faster
- SCP reduction = 20.54%
- paired p = 0.0114
- statistically significant


Native SCP showed a measurable reduction in SCP-related execution time, and the reduction became statistically significant in the separate no-Vitest diagnostic analysis. In the complete Vitest-enabled main evaluation, the measured performance difference was smaller and was not statistically significant.


---

## 9. Answer to Research Question 3

The current answer to RQ3 is:

Replacing Docker SCP with Native SCP produced lower mean execution times while maintaining the required build, test, and deployment quality.

In the main 14-by-14 Vitest-enabled evaluation:

- workflow duration decreased by 2.72%
- resource-use proxy decreased by 2.06%
- SCP-related duration decreased by 6.62%

These differences were not statistically significant.

All 28 main evaluation runs passed the required quality checks.

The separate no-Vitest diagnostic analysis showed a larger 20.54% reduction in SCP-related duration, and this diagnostic difference was statistically significant.

Native SCP showed evidence of lower execution time, especially at the SCP stage, while maintaining quality. However, the final main evaluation does not provide enough evidence to claim a statistically significant overall workflow performance improvement.

---

## 10. Connection with Chapter 6

Chapter 6 selected Native SCP as the optimization based on the earlier controlled Docker-versus-Native experiment.

Chapter 6 result:

- Native SCP mean: 19.50 s
- Docker SCP mean: 27.40 s
- reduction: 28.83%
- p < 0.001
- 95% CI: -10.39 to -5.41 s

Chapter 7 tested the selected optimization more formally with the Vitest quality gate enabled.

The Chapter 7 main result was weaker:

- Native SCP mean: 21.14 s
- Docker SCP mean: 22.64 s
- reduction: 6.62%
- p = 0.1558

The no-Vitest diagnostic result was closer to the Chapter 6 finding:

- Native SCP mean: 21.00 s
- Docker SCP mean: 26.43 s
- reduction: 20.54%
- paired p = 0.0114

This difference between the experiments is important for Chapter 8.

It shows that the measured size of the optimization effect changed between the different controlled datasets.

###

---

## Current overall thesis position

The practical thesis work now forms a clear chain:

**Historical workflow data → anomaly analysis → SCP investigation → evidence-based optimization selection → controlled evaluation → quality verification → final discussion**

RQ1 identifies the unusual workflow behaviour.

RQ2 evaluates how Isolation Forest supports anomaly identification compared with IQR.

RQ3 evaluates the measurable effect of the selected Native SCP optimization.

The main technical experimentation is now largely complete.

The next major task is to complete the methodology documentation and write the final discussion and conclusions.
