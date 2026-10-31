# 4 DATA, METHODS AND EVALUATION PLAN

## 4.1 Research and Development Approach

This thesis uses a case study approach that focuses on the iSign frontend CI/CD workflow. The work uses both quantitative measurement and qualitative analysis. Quantitative methods are used to look at historical GitHub Actions execution data, and qualitative analysis is used to understand unusual workflow behaviour and find possible causes. The development work follows an iterative development approach, where the analysis results are used to guide the selection, implementation and evaluation of one practical CI/CD optimization.

Isolation Forest is used in this thesis as a method for finding anomalies, but it is not the main research approach of the study. A simple statistical method based on the interquartile range is used as a baseline, and its results are compared with the Isolation Forest results. The purpose of this comparison is to see how well the machine-learning method helps to identify unusual workflow behaviour compared with a simpler statistical approach.


## 4.2 Data Sources and Dataset Selection

The main dataset for this thesis comes from the iSign frontend GitHub Actions workflow. Historical data about workflow runs, jobs and steps were collected from the frontend repository. The frontend workflow was selected because it had enough similar historical runs for analysis, while the backend workflow had a smaller number of reliable full runs during the selected period. Because of this, the iSign frontend dataset is used as the main case-study dataset for finding unusual behaviour and evaluating the optimization carried out at a later stage.
A public GitHub Actions dataset from the FastAPI project is used as a supporting reference dataset. The data comes from the `Test` workflow and focuses on runs triggered by pull requests during the selected study period. After checking the workflow structure, 316 runs were found to have the required similar test-job structure. This dataset is used to support the development and testing of the analysis method before it is applied to the iSign case. It is not considered a second case study, and no optimization is carried out on the FastAPI project.

## 4.3 Data Collection and Preprocessing

## 4.4 Statistical Baseline and Isolation Forest Analysis

## 4.5 Comparison of Analysis Methods

## 4.6 Optimization Evaluation Plan
