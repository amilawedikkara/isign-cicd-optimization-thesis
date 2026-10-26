# Thesis Alignment and Technical Decisions

This document summarizes the current thesis position, the points that are already aligned, and the remaining technical decisions that need to be finalized before continuing the implementation and evaluation work.

## 1. Points Already Aligned

| Thesis guidance | How my thesis currently aligns |
|---|---|
| 1. The thesis should focus on one clearly defined development task. | I have limited the thesis to analysing and optimizing one GitHub Actions workflow in the iSign frontend repository. The `Deploy to Dev Apache Server` workflow on the `development` branch remains the main and only case study. |
| 2. The starting situation should be documented clearly. | I have documented the selected repository, branch, workflow file, trigger, jobs, steps, deployment behaviour, execution environment and available historical workflow runs. |
| 3. My earlier project work and new thesis contribution should be clearly separated. | My earlier iSign project and internship work are treated as the starting situation. The thesis contribution begins with CI/CD data collection, preprocessing, statistical analysis, Isolation Forest analysis, technical investigation, optimization and evaluation. |
| 4. The main objective should be a Python-based analysis tool plus one justified optimization. | The thesis objective follows this structure: develop and evaluate a Python-based AI-assisted CI/CD analysis tool using Isolation Forest, and then implement and measure one evidence-based iSign optimization. |
| 5. Three research or development questions are sufficient. | The thesis uses three research questions:<br>**RQ1.** What inefficient or unusual behaviour can be identified in the selected iSign frontend GitHub Actions workflow?<br>**RQ2.** How does Isolation Forest support the identification of unusual workflow behaviour compared with a simple statistical baseline method?<br>**RQ3.** What measurable effect does one evidence-based CI/CD optimization have on workflow duration and resource use, while maintaining the required build, test, and deployment quality? |
| 6. The usefulness of the AI-assisted analysis should be separated from the effect of the optimization. | RQ2 evaluates the analysis method. RQ3 separately evaluates the effect of the implemented pipeline optimization. |
| 7. One primary AI/ML approach should be used. | Isolation Forest remains the only machine-learning method in the thesis. I am not adding additional ML models or an LLM-based pipeline-analysis method. |
| 8. The AI method should be compared with a simple baseline. | I use descriptive statistics and IQR-based outlier detection as the simple statistical baseline for comparison with Isolation Forest. |
| 9. The iSign historical dataset is sufficient for the core case-study analysis. | I have 55 historical frontend workflow runs, of which 33 are comparable successful full runs with 495 step-level observations. These 33 runs are sufficient for descriptive statistics, IQR analysis, Isolation Forest analysis, anomaly investigation and identifying an optimization candidate. |
| 10. An anomaly should not automatically be treated as an inefficiency. | I have identified unusual iSign runs, but I have not classified them as inefficiencies. The flagged runs will first be investigated using job durations, step durations, workflow configuration and logs. |
| 11. GitHub Actions data should be collected consistently and reruns should be handled correctly. | The Python data-collection and preprocessing work records run, job and step information, including identifiers, commits, triggers, outcomes, timestamps and durations. Rerun timing has also been handled consistently. |
| 12. A public dataset must not replace the iSign case. | FastAPI does not replace iSign and will not be used for an optimization. Any FastAPI use is only supporting work for evaluating the analysis method. The actual inefficiency, optimization and before/after measurements remain in iSign. |
| 13. One optimization should be selected only after analysing the findings. | No optimization has been selected yet. SCP duration is currently only an investigation candidate. The final optimization will be selected only after technical investigation shows a real improvement opportunity. |
| 14. Workflow speed and resource use should be treated as different measurements. | RQ3 separates workflow elapsed duration from resource use. The historical 33 runs provide the current iSign baseline for RQ1 and RQ2. For RQ3, we still need to confirm whether these runs are suitable as the pre-optimization baseline or whether additional controlled pre-optimization runs should be collected. |
| 15. The optimization must be evaluated without reducing required software quality. | The before/after evaluation will preserve required build, test, workflow and deployment quality. The optimization will not be justified by simply removing important quality checks. |

## 2. Five Technical Decisions to Finalize



| Point to finalize | Current proposed approach |
|---|---|
| 1. Exact role of the FastAPI public dataset in RQ2. | Use FastAPI only as a larger external robustness check for the IQR versus Isolation Forest comparison. Freeze the analysis approach, apply the same logic to the larger FastAPI dataset, compare the behaviour of the two methods, and stop the FastAPI work there. No FastAPI optimization will be performed. |
| 2. Simple statistical baseline for comparison with Isolation Forest. | Keep the existing IQR method (`Q3 + 1.5 * IQR`) as the simple statistical baseline. It is already implemented, easy to reproduce and easy to explain. No additional statistical baseline will be added unless there is a methodological reason. |
| 3. Resource-use metric for RQ3. | Use total job execution time - the sum of all job durations in one workflow run - as a practical substitute for resource use. This is used because exact CPU, memory, or infrastructure resource consumption is not available. Report this separately from total workflow elapsed duration. Record the Python analysis tool execution time separately as the cost of running the analysis. |
| 4. RQ3 pre-optimization baseline and number of controlled runs. | For RQ3, we still need to decide whether the existing 33 historical runs are suitable as the before-optimization baseline, or whether we should first collect new controlled runs of the current workflow under the same test, build and deployment conditions that will also be used after the optimization. The final number of comparable before-and-after runs will be confirmed before implementation. |
| 5. Exact RQ3 evaluation metrics and quality baseline. | **Workflow duration:** total workflow elapsed time; **Resource use:** sum of job execution times; **Build quality:** frontend build succeeds; **Test quality:** same Vitest suite and test count pass and coverage is recorded where available; **Deployment quality:** deployment and verification succeed; **Reliability:** failures and reruns are recorded; **Optimization effect:** before-and-after differences are calculated. |

## 3. Expected Thesis Outputs

The expected thesis outputs are:

- a Python-based AI-assisted CI/CD analysis tool
- statistical analysis of pipeline data
- an evaluated Isolation Forest anomaly-detection component
- identified CI/CD inefficiencies or anti-patterns
- at least one implemented iSign CI/CD optimization
- before-and-after measurements
- measured evaluation results
- recommendations for future iSign pipeline improvements

## 4. Current Technical Direction

The current planned development flow is:

**iSign baseline data -> statistical analysis -> Isolation Forest analysis -> comparison and technical investigation -> identify a real iSign inefficiency -> select one justified optimization -> implement the optimization -> perform repeated before-and-after measurements -> evaluate the results -> answer RQ1, RQ2 and RQ3 -> provide recommendations.**

## 5. Work Remaining After the Alignment Is Confirmed

1. Complete the technical investigation of the already flagged iSign runs.
2. Determine whether SCP or another workflow component represents a real inefficiency or anti-pattern.
3. Select one evidence-based optimization.
4. Add literature specifically supporting the selected optimization.
5. Freeze the final before/after metrics and controlled experiment conditions.
6. Perform controlled pre-optimization measurements.
7. Implement the selected optimization.
8. Perform controlled post-optimization measurements.
9. Calculate and interpret the measured effect.
10. Answer RQ1, RQ2 and RQ3.
11. Produce recommendations for future iSign pipeline improvements.
12.
