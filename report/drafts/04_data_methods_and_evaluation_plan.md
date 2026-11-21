# 4 DATA, METHODS AND EVALUATION PLAN

## 4.1 Research and Development Approach

This thesis uses a case study approach that focuses on the iSign frontend CI/CD workflow. The work uses both quantitative measurement and qualitative analysis. Quantitative methods are used to look at historical GitHub Actions execution data, and qualitative analysis is used to understand unusual workflow behaviour and find possible causes. The development work follows an iterative development approach, where the analysis results are used to guide the selection, implementation and evaluation of one practical CI/CD optimization.

Isolation Forest is used in this thesis as a method for finding anomalies, but it is not the main research approach of the study. A simple statistical method based on the interquartile range is used as a baseline, and its results are compared with the Isolation Forest results. The purpose of this comparison is to see how well the machine-learning method helps to identify unusual workflow behaviour compared with a simpler statistical approach.


## 4.2 Data Sources and Dataset Selection

The main dataset for this thesis comes from the iSign frontend GitHub Actions workflow. Historical data about workflow runs, jobs and steps were collected from the frontend repository. The frontend workflow was selected because it had enough similar historical runs for analysis, while the backend workflow had a smaller number of reliable full runs during the selected period. Because of this, the iSign frontend dataset is used as the main case-study dataset for finding unusual behaviour and evaluating the optimization carried out at a later stage.
A public GitHub Actions dataset from the FastAPI project is used as a supporting reference dataset. The data comes from the `Test` workflow and focuses on runs triggered by pull requests during the selected study period. After checking the workflow structure, 316 runs were found to have the required similar test-job structure. This dataset is used to support the development and testing of the analysis method before it is applied to the iSign case. It is not considered a second case study, and no optimization is carried out on the FastAPI project.

## 4.3 Data Collection and Preprocessing

Historical execution data was collected from the selected iSign frontend GitHub Actions workflow. The data included workflow runs, jobs and individual workflow steps. Timing information was taken from these different levels because the analysis needed to look at the full workflow, but also at the execution time of the main individual steps.

The original frontend dataset contained 55 workflow runs. Not all of them could be used for a fair comparison. Runs that were not successful comparable full executions were removed from the main analysis. After filtering, 33 workflow runs remained and these produced 495 step-level observations. This filtering was important. The statistical and machine-learning methods needed runs that carried out the same type of workflow work, otherwise the timing comparison could become misleading.

For the direct comparison between IQR and Isolation Forest, the same five timing features were used for every included run. These were SCP action setup, Node.js setup, dependency installation, React build and SCP transfer. Both methods therefore worked with the same measurements. This made the comparison more consistent and helped to avoid differences caused simply by using different workflow features.

The public FastAPI GitHub Actions data was handled separately as supporting reference data. Its workflow structure was checked first, and 316 runs with a similar required test-job structure were kept. The dataset was mainly used to support development and testing of the analysis approach before it was applied to the iSign case. It was not considered another case study. No optimization was carried out on the FastAPI project.

## 4.4 Statistical Baseline and Isolation Forest Analysis

The interquartile range method was used as the simple statistical baseline. For each selected timing feature, the first quartile (Q1), third quartile (Q3), and interquartile range were calculated. The IQR was calculated by subtracting Q1 from Q3. Lower and upper fences were then formed using Q1 - 1.5 × IQR and Q3 + 1.5 × IQR. Any timing value outside these limits was treated as a possible outlier.

For the common-feature comparison, a workflow run was flagged by IQR if at least one of the five timing values was outside its lower or upper fence. Values exactly on the fence were not treated as outside the limit. This gives a simple way to notice unusually high or low execution times in individual workflow steps.

Isolation Forest was applied to the same 33 comparable runs and the same five timing features. The model used 100 estimators, automatic contamination, and a random state of 42. The fixed random state was used to keep the analysis reproducible. With the same dataset and settings, the method should return the same classification result.

Isolation Forest was used as an unsupervised method because verified labels for normal and anomalous workflow runs were not available. IQR checks each timing feature separately. Isolation Forest works differently, as it considers all five timing values together as one combined pattern. Using the same runs and the same features for both methods made the comparison more direct and easier to interpret.

## 4.5 Comparison of Analysis Methods

IQR and Isolation Forest were compared using the same 33 iSign workflow runs and the same five timing features. This kept the comparison fair. Each method produced a run-level classification showing whether a run was treated as normal or unusual.

The classifications were compared run by run. The comparison included runs flagged by both methods, runs flagged only by IQR, runs flagged only by Isolation Forest, and runs classified as normal by both methods. An overall agreement rate was also calculated by counting the runs where both methods gave the same classification.

The disagreement cases were examined separately. This was important because the two methods look at timing data in different ways. IQR checks individual timing values against statistical limits, while Isolation Forest considers the combined pattern of all five features. These disagreement cases therefore helped to show what type of unusual behaviour each method could identify.

Verified ground-truth labels were not available for the workflow runs. Because of this, accuracy, precision and recall were not calculated. The purpose was not to prove that one method was more accurate than the other. The aim was to examine how Isolation Forest supported the identification of unusual workflow behaviour compared with the simpler IQR baseline.

## 4.6 Optimization Evaluation Design

The selected Native SCP optimization was tested against the previous Docker SCP method under controlled conditions. The other main parts were kept the same for both workflows: frontend project, Node.js setup, dependencies, React build, development server, deployment target, synchronization and verification. The main technical change was the SCP implementation. Runs were carried out one by one. The order was alternated between Docker and Native so that one method was not always tested first.

The main evaluation included 14 Docker SCP runs and 14 Native SCP runs. Vitest was enabled in both workflows with the same command and test selection. It was used as a common quality gate and was not part of the SCP optimization. Performance was evaluated using total workflow duration, total job execution time as a resource-use proxy, and SCP-related duration. Direct CPU and memory measurements were not available, so the resource-use proxy was treated only as an indirect measure.

Descriptive statistics were calculated for the main performance measures. Mean, median, standard deviation, minimum, maximum and range were used to describe the results. Welch's two-sample t-test was then used to compare Docker SCP and Native SCP. A significance level of 0.05 and 95% confidence intervals were used to evaluate whether the observed differences were statistically significant.

Quality was checked separately from execution time. Vitest success, frontend build success, SCP transfer, file synchronization, deployment verification and complete job success were checked for both methods. A separate seven-pair no-Vitest diagnostic comparison was also carried out to examine SCP-related timing with fewer unrelated workflow components. These diagnostic runs were kept outside the main evaluation dataset and were used only as supporting evidence.
