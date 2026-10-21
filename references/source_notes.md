# Source S001

## Basic information

Author / Organization: Mojtaba Shahin, Muhammad Ali Babar, Liming Zhu
Year: 2017
Title: Continuous integration, delivery and deployment: a systematic review on approaches, tools, challenges and practices
Source type: Peer-reviewed systematic literature review
Journal / Publisher: IEEE Access
Volume: 5
Pages: 3909-3943
Article number: 7884954
DOI: 10.1109/ACCESS.2017.2685629

Primary source page:
https://research.monash.edu/en/publications/continuous-integration-delivery-and-deployment-a-systematic-revie/

DOI link:
https://doi.org/10.1109/ACCESS.2017.2685629

Publisher:
IEEE Access

Accessed: 21 October 2026

## Thesis topic

Relevant section:

- Introduction
- Knowledge Base
- CI/CD performance measurement

## What this source supports

- Continuous integration, delivery and deployment are important software-development practices.
- Continuous practices support frequent and reliable software delivery.
- Build and test time, automated testing, visibility and deployment reliability are important concerns.

## My understanding

CI/CD, which refers to continuous integration, delivery and deployment, helps software teams deliver software frequently and reliably. It supports this by automating activities such as integrating code, testing software and supporting the release process. However, continuous practices also involve practical challenges. For example, builds and tests may take too long, automated testing requires effective support, build and test results need to be clearly visible, and deployment reliability can be a concern. Because of these issues, the performance and reliability of CI/CD pipelines are important areas for systematic analysis.

## Citation status

Read: Yes
Used in thesis: No
Reference checked: Yes

# Source S002

## Basic information

Author / Organization: Eliezio Soares, Gustavo Sizilio, Jadson Santos, Daniel Alencar da Costa, Uirá Kulesza  
Year: 2022  
Title: The effects of continuous integration on software development: a systematic literature review  
Source type: Peer-reviewed systematic literature review  
Journal / Publisher: Empirical Software Engineering  
Volume: 27  
Article: 78  
DOI: 10.1007/s10664-021-10114-1

## Source access

Primary source page:  
https://link.springer.com/article/10.1007/s10664-021-10114-1

DOI link:  
https://doi.org/10.1007/s10664-021-10114-1

Publisher:  
Springer Nature / Empirical Software Engineering

Accessed:  
21 October 2026

## Thesis topic

Relevant section:

- Introduction
- Knowledge Base
- Continuous Integration

## What this source supports

- Continuous Integration has been widely studied in empirical software-engineering research.
- CI can provide positive effects on software development practices and processes.
- CI can also introduce technical and process-related challenges.
- The effects of CI can be considered across areas such as development activities, software processes, quality assurance, integration patterns, defects, and build patterns.

## My understanding

This study shows that Continuous Integration has been widely researched and can bring several benefits to software development. It can improve development activities, software processes, and quality assurance, but it can also create technical and process-related challenges. The study also shows that the effects of CI are not limited to a single area, as CI can influence build patterns, defects, integration practices, and other parts of the development process.

## Citation status

Read: Yes  
Used in thesis: No  
Reference checked: Yes

# Source S003

## Basic information

Author / Organization: Sebastian Elbaum, Gregg Rothermel, John Penix  
Year: 2014  
Title: Techniques for improving regression testing in continuous integration development environments  
Source type: Peer-reviewed conference paper  
Conference / Publisher: Proceedings of the 22nd ACM SIGSOFT International Symposium on Foundations of Software Engineering (FSE 2014)  
Pages: 235-245  
DOI: 10.1145/2635868.2635910

## Source access

Primary source page:  
https://research.google/pubs/techniques-for-improving-regression-testing-in-continuous-integration-development-environments/

DOI link:  
https://doi.org/10.1145/2635868.2635910

Publisher:  
ACM

Accessed:  
21 October 2026

## Thesis topic

Relevant section:

- Introduction
- Knowledge Base
- Continuous Integration
- Fast feedback in CI/CD

## What this source supports

- Continuous Integration involves frequent integration of new or changed code with the main codebase.
- Testing is important before and after code integration.
- Fast feedback is an important benefit of Continuous Integration.
- Long or inefficient testing can delay feedback to developers.
- Regression-test selection and prioritization can help make CI testing more cost-effective.

## My understanding

Continuous Integration means that developers frequently merge new or changed code into the main codebase, and testing is important both before and after this integration. Fast feedback is one of the main benefits of CI, but slow or inefficient testing can delay that feedback. The source also explains that regression-test selection and test-case prioritization can make CI testing more cost-effective, and the authors present algorithms to support this process.

## Citation status

Read: Yes  
Used in thesis: No  
Reference checked: Yes

# Source S004

## Basic information

Author / Organization: Martin Fowler
Year: 2024
Title: Continuous Integration
Source type: Practitioner / technical web article
Website / Publisher: MartinFowler.com

## Source access

Primary source page:
https://martinfowler.com/articles/continuousIntegration.html

Accessed:
21 October 2026

## Thesis topic

Relevant section:

- Introduction
- Knowledge Base
- Continuous Integration
- Fast feedback in CI/CD
- CI/CD performance measurement

## What this source supports

- Continuous Integration is a software-development practice in which developers integrate their changes into a shared codebase frequently.
- Each integration should be verified using an automated build, including automated tests.
- Frequent integration helps detect integration problems earlier.
- Every push to the mainline can trigger an automated CI build.
- Rapid feedback is an important goal of Continuous Integration.
- Long-running builds delay feedback and can reduce the practical benefits of CI.
- Build status and results should be visible to the development team.

## Why this source is relevant to the thesis

The selected iSign workflow is implemented using GitHub Actions and performs automated CI/CD activities. The thesis measures workflow and step execution times, so Fowler's discussion of rapid feedback and keeping builds fast provides useful theoretical background for why pipeline execution time matters.

The source also supports the idea that pipeline speed should be considered together with automated verification rather than simply making the workflow faster by removing necessary checks.

## My understanding

Continuous Integration is a practice in which developers frequently integrate their changes into a shared mainline codebase, and each integration is verified by an automated build and tests. Every push to the mainline should trigger a CI build, and the build should remain fast so that developers receive feedback quickly. The build status and results should also be visible to the whole team so that everyone can easily understand the current state of the integration process.

## Citation status

Read: Yes
Used in thesis: No
Reference checked: Yes

# Source S005

## Basic information

Author / Organization: Jez Humble, David Farley  
Year: 2010  
Title: Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation  
Source type: Book  
Publisher: Addison-Wesley Professional  
Edition: 1st edition  
ISBN: 978-0-321-60191-9

## Source access

Primary publisher page:
https://www.pearson.com/en-gb/subject-catalog/p/continuous-delivery-reliable-software-releases-through-build-test-and-deployment-automation/P200000009113/9780321601919

Alternative publisher page:
https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919

Accessed:
21 October 2026

## Local copy

Local file:
references/project_materials/literature/Humble_Farley_Continuous_Delivery_2010.pdf

Relevant reading:

- Preface / Introduction
- Chapter 5: Anatomy of the Deployment Pipeline
- Metrics section

Local file tracked by Git:
No

## Thesis topic

Relevant section:

- Introduction
- Knowledge Base
- Continuous Delivery
- CI/CD reliability
- Deployment automation
- Before/after evaluation

## What this source supports

- Continuous Delivery aims to make software release reliable, repeatable, and low risk.
- Build, testing, and deployment activities should be automated where appropriate.
- A deployment pipeline helps manage software changes from integration toward release.
- Fast feedback is important when problems occur.
- Pipeline performance should not be evaluated only by speed; software quality and release reliability must also be maintained.
- Small and frequent changes can support safer and more manageable delivery.

## Why this source is relevant to the thesis

The selected iSign workflow includes both build and deployment activities. This source supports the idea that an optimization should not only reduce execution time but should also preserve reliable build, testing, and deployment behaviour.

This is directly relevant to the planned before-and-after evaluation of the selected iSign CI/CD optimization.

## My understanding

Continuous Delivery aims to make software releases reliable and low risk by automating build, testing, and deployment activities. A deployment pipeline helps move software changes from integration towards release in a controlled and repeatable way, and fast feedback is important so that problems can be identified quickly. The source also shows that pipeline performance should not be judged only by speed, because software quality and release reliability must also be maintained. It also emphasizes frequent and incremental delivery as a way to improve the software delivery process.

## Citation status

Read: No  
Used in thesis: No  
Reference checked: Yes

# Source S006

## Basic information

Author / Organization: GitHub
Year: 2026
Title: Workflows
Source type: Official technical documentation
Website / Publisher: GitHub Docs

## Source access

Primary source page:
https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows

Accessed:
21 October 2026

## Thesis topic

Relevant section:

- Knowledge Base
- GitHub Actions
- Data and Methods
- Workflow structure
- Workflow, job, and step-level analysis

## What this source supports

- A GitHub Actions workflow is an automated process defined in a YAML file.
- Workflows are stored in the `.github/workflows` directory.
- A workflow can be triggered by repository events, manually, or on a schedule.
- A workflow contains one or more jobs.
- Each job runs on a runner and contains one or more steps.
- A step can execute a script or a reusable GitHub Action.
- Jobs can be configured to run independently, sequentially, or with dependencies.
- Workflow runs are created when configured trigger conditions are met.

## Why this source is relevant to the thesis

The selected iSign CI/CD process is implemented with GitHub Actions. The thesis collects and analyzes data at workflow, job, and step level. Therefore, the official GitHub Actions structure provides the technical basis for explaining how the collected data is organized.

The same hierarchy is used in the thesis analysis:

Workflow
→ Workflow Run
→ Job
→ Step

## My understanding

A GitHub Actions workflow is an automated process defined in a YAML file and stored in the `.github/workflows` directory of a repository. A workflow can be triggered by repository events, manually, or according to a schedule, and it contains one or more jobs. Each job runs on a runner and includes one or more steps, while each step can execute a script or a reusable action. This structure is relevant to the thesis because the iSign CI/CD data is organized using the same hierarchy: workflow, workflow run, job, and step.

## Citation status

Read: Yes
Used in thesis: No
Reference checked: Yes

# Source S007

## Basic information

Author / Organization: GitHub  
Year: 2026  
Title: REST API endpoints for workflow runs and workflow jobs  
Source type: Official technical documentation  
Website / Publisher: GitHub Docs

## Source access

Workflow runs documentation:
https://docs.github.com/en/rest/actions/workflow-runs

Workflow jobs documentation:
https://docs.github.com/en/rest/actions/workflow-jobs

Accessed:
21 October 2026

## Thesis topic

Relevant section:

- Data and Methods
- GitHub Actions data collection
- Workflow-run data
- Job-level data
- Reproducible data collection

## What this source supports

- The GitHub REST API can be used to retrieve GitHub Actions workflow runs.
- Workflow runs can be filtered using properties such as branch, event, status, and creation time.
- A workflow run represents one execution of a workflow.
- The API can return jobs belonging to a workflow run.
- A workflow job contains a set of steps that execute on the same runner.
- Workflow and job information can be collected programmatically instead of inspected manually.
- Read access to the repository is sufficient for retrieving this information when the required permissions are available.

## Why this source is relevant to the thesis

The thesis uses the GitHub API to collect historical iSign GitHub Actions data. The Python collection script retrieves workflow-run information and job-level information so that comparable runs can be selected and execution durations can be calculated.

This source provides the official technical documentation for the API used in the thesis data-collection method.

## My understanding

The GitHub REST API can be used to collect GitHub Actions workflow runs, and these runs can be filtered by branch, event, status, and creation time. A workflow run represents one execution of a workflow, and the API can also return the jobs that belong to that run. Each job contains a set of steps that execute on the same runner, so workflow and job data can be collected programmatically instead of manually. This supports the thesis data-collection process because historical iSign workflow-run and job-level data can be retrieved using a Python script.

## Citation status

Read: Yes  
Used in thesis: No  
Reference checked: Yes

# Source S008

## Basic information

Author / Organization: Taher Ahmed Ghaleb, Daniel Alencar da Costa, Ying Zou  
Year: 2019  
Title: An empirical study of the long duration of continuous integration builds  
Source type: Peer-reviewed journal article  
Journal: Empirical Software Engineering  
Volume: 24  
Issue: 4  
Pages: 2102–2139  
Publisher: Springer Nature  
DOI: 10.1007/s10664-019-09695-9

## Source access

Primary source page:
https://link.springer.com/article/10.1007/s10664-019-09695-9

University repository page:
https://ourarchive.otago.ac.nz/esploro/outputs/journalArticle/An-empirical-study-of-the-long/9926515039601891

DOI:
https://doi.org/10.1007/s10664-019-09695-9

Accessed:
21 October 2026

## Thesis topic

Relevant section:

- Knowledge Base
- CI/CD performance
- Build duration
- Pipeline optimization
- Bottleneck investigation
- Before/after evaluation

## What this source supports

- Long CI build durations can delay developer feedback and affect development work.
- Build duration is an important CI performance concern.
- The study analysed 104,442 CI builds from 67 GitHub projects.
- Several factors can be associated with long build durations.
- Repeated execution of failed commands was strongly associated with longer builds.
- Build configuration choices can affect CI duration.
- Caching content that does not frequently change may help reduce build duration.
- Finishing builds when all required jobs are complete may also improve build performance.
- CI optimization should be based on evidence from the actual build process.

## Why this source is relevant to the thesis

The iSign thesis measures workflow, job, and step execution durations to identify unusual or inefficient behaviour. This study provides academic support for treating CI build duration as a meaningful performance metric and for investigating the causes of unusually long builds before selecting an optimization.

It also supports the evidence-based approach used in the thesis: first measure and analyse the existing CI behaviour, then identify a suitable optimization.

## My understanding

Continuous Integration helps teams build software frequently, but long build durations can delay feedback and prevent developers from focusing on other important work. The source studies 104,442 CI builds from 67 GitHub projects and shows that several factors can be associated with long build durations, not only commonly considered factors such as project size or test density. It also finds that repeatedly rerunning failed commands is strongly associated with longer builds, while caching content that does not change frequently and completing builds as soon as all required jobs have finished may help reduce build duration. The source suggests that developers should use appropriate CI build configurations and that tool developers should provide support for identifying cacheable parts of a project.

## Citation status

Read: Yes
Used in thesis: No  
Reference checked: Yes

# Source S009

## Basic information

Author / Organization: Fei Tony Liu, Kai Ming Ting, Zhi-Hua Zhou  
Year: 2008  
Title: Isolation Forest  
Source type: Peer-reviewed conference paper  
Conference: 2008 Eighth IEEE International Conference on Data Mining (ICDM)  
Pages: 413–422  
Publisher: IEEE  
DOI: 10.1109/ICDM.2008.17

## Source access

IEEE Xplore:
https://ieeexplore.ieee.org/document/4781136

University research record:
https://research.monash.edu/en/publications/isolation-forest/

DOI:
https://doi.org/10.1109/ICDM.2008.17

Accessed:
21 October 2026

## Thesis topic

Relevant section:

- Knowledge Base
- Anomaly detection
- Unsupervised machine learning
- Isolation Forest
- Analysis method
- Statistical baseline vs Isolation Forest

## What this source supports

- Isolation Forest is an anomaly-detection method.
- Unlike methods that first model normal data, Isolation Forest directly attempts to isolate unusual observations.
- Anomalies are generally easier to isolate because they are different from normal observations.
- The method uses random partitioning of the data.
- Anomalous observations tend to require shorter paths in the isolation trees.
- Isolation Forest does not require labelled anomaly examples for training.
- The method is computationally efficient and has relatively low memory requirements.
- The original study showed competitive anomaly-detection performance compared with several other methods.

## Why this source is relevant to the thesis

Isolation Forest is the AI-assisted anomaly-detection method used in the thesis. This original paper provides the theoretical basis for explaining how the method works and why it can be applied to historical CI/CD execution-time data without manually labelling every run as normal or anomalous beforehand.

It also supports the comparison between the simple statistical baseline and the Isolation Forest method.

## My understanding

Isolation Forest is an anomaly-detection method that works differently from methods that first build a profile of normal data. Instead of profiling normal observations, it directly attempts to isolate anomalies by randomly partitioning the data, and anomalous observations tend to be isolated using shorter paths in the isolation trees. The method does not require labelled anomaly examples for training, and it is computationally efficient with relatively low memory requirements. The original study also showed that Isolation Forest performed competitively compared with several other methods, particularly on large datasets and high-dimensional problems.

## Citation status

Read: Yes
Used in thesis: No
Reference checked: Yes

# Source S010

## Basic information

Author / Organization: Varun Chandola, Arindam Banerjee, Vipin Kumar  
Year: 2009  
Title: Anomaly Detection: A Survey  
Source type: Peer-reviewed review article  
Journal: ACM Computing Surveys  
Volume: 41  
Issue: 3  
Article: 15  
Publisher: Association for Computing Machinery (ACM)  
DOI: 10.1145/1541880.1541882

## Source access

Primary research record:
https://experts.umn.edu/en/publications/anomaly-detection-a-survey/

DOI:
https://doi.org/10.1145/1541880.1541882

Accessible paper copy:
https://arindam.cs.illinois.edu/papers/09/anomaly.pdf

Accessed:
21 October 2026

### Local copy

Local file:
references/project_materials/literature/anomaly.pdf

Local file tracked by Git:
No

## Thesis topic

Relevant section:

- Knowledge Base
- Anomaly detection
- Normal and anomalous behaviour
- Unsupervised anomaly detection
- Selection of anomaly-detection methods

## What this source supports

- Anomaly detection aims to identify patterns that do not conform to expected behaviour.
- Anomalies may also be called outliers, exceptions, or unusual observations.
- Many different anomaly-detection techniques exist.
- Different techniques rely on different assumptions about normal and anomalous behaviour.
- The suitability of a technique depends on the characteristics of the data and application domain.
- Anomaly detection can be applied across many different domains.
- Computational complexity is also an important consideration when selecting an anomaly-detection method.

## Why this source is relevant to the thesis

The thesis aims to identify unusual behaviour in historical CI/CD execution-time data. This source provides a general academic foundation for defining anomaly detection and explaining why the selected detection method must be appropriate for the available data.

It also helps position Isolation Forest as one anomaly-detection technique within a broader group of available approaches.

## My understanding

Anomaly detection is an important problem that has been studied in many different research areas, and its main aim is to identify patterns that do not conform to expected behaviour. Many different techniques exist, and they can be grouped into categories based on their underlying approaches. Each technique makes different assumptions about normal and anomalous behaviour, so the suitability of a method depends on the characteristics of the data and the application domain. The survey also shows that computational complexity is an important factor to consider when selecting an anomaly-detection method.

## Citation status

Read: Yes
Used in thesis: No  
Reference checked: Yes

# Source S011

## Basic information

Author / Organization: NIST / SEMATECH
Year: n.d.
Title: What are outliers in the data?
Source type: Official statistical handbook / technical web resource
Publisher: National Institute of Standards and Technology (NIST)

## Source access

Primary source page:
https://www.itl.nist.gov/div898/handbook/prc/section1/prc16.htm

Accessed:
21 October 2026

## Thesis topic

Relevant section:
- Knowledge Base
- Statistical analysis
- Outlier detection
- Interquartile Range (IQR)
- Statistical baseline
- Comparison with Isolation Forest

## What this source supports

- An outlier is an observation that is unusually far from other observations.
- Normal behaviour should first be understood before unusual observations are identified.
- The interquartile range is calculated as Q3 - Q1.
- Q1 represents the 25th percentile and Q3 represents the 75th percentile.
- An inner upper fence can be calculated as Q3 + 1.5 × IQR.
- An inner lower fence can be calculated as Q1 - 1.5 × IQR.
- Observations outside these inner fences can be treated as potential outliers.
- Outliers should be investigated instead of automatically being removed, because they may contain useful information.

## Why this source is relevant to the thesis

The thesis uses the IQR method as a simple statistical baseline for identifying unusual CI/CD execution times.

For the analysis of unusually slow iSign runs, the main threshold used is:

Upper threshold = Q3 + 1.5 × IQR

Runs above this threshold are treated as candidates for further investigation. The statistical results can later be compared with the results produced by Isolation Forest.

## My understanding

an outlier is an observation that is very far away from the other observations in a data set. Before we can find unusual points, we first need to understand what normal behaviour looks like, and the interquartile range (Q3 minus Q1) is used together with the lower and upper fences (Q1 - 1.5×IQR and Q3 + 1.5×IQR) to identify possible outliers. Observations outside these fences can be treated as potential outliers, but they should be investigated carefully instead of being removed automatically, because they may contain useful information about the process or the data collection.


## Citation status

Read: Yes
Used in thesis: No
Reference checked: Yes

# Source S012

## Basic information

Author / Organization: scikit-learn developers
Year: 2026
Title: IsolationForest
Source type: Official software documentation
Website / Publisher: scikit-learn

## Source access

Primary documentation:
https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html

Accessed:
21 October 2026

## Thesis topic

Relevant section:
- Data and Methods
- Isolation Forest implementation
- Python analysis tool
- Model parameters
- Reproducibility

## What this source supports

- `IsolationForest` is available in `sklearn.ensemble`.
- The implementation isolates observations by randomly selecting features and split values.
- Anomalous observations usually have shorter isolation paths.
- `n_estimators` controls the number of trees.
- `max_samples` controls how many observations are used to train each tree.
- `contamination` is used when defining the anomaly threshold.
- `random_state` controls the random behaviour of the model.
- Setting `random_state` to a fixed integer helps make repeated analyses reproducible.
- `predict()` returns `1` for inliers and `-1` for outliers.
- Lower anomaly scores represent more abnormal observations.

## Why this source is relevant to the thesis

The thesis implements Isolation Forest using Python and scikit-learn. This documentation provides the technical basis for explaining the model parameters used in the implementation and for making the analysis reproducible.

This source complements the original Isolation Forest research paper by documenting the software implementation actually used in the thesis.

## My understanding

`IsolationForest` from `sklearn.ensemble` detects anomalies by randomly selecting features and split values to isolate observations, and anomalous points usually have shorter isolation paths. The model has several important parameters: `n_estimators` controls the number of trees, `max_samples` controls how many observations are used for each tree, and `contamination` helps define the anomaly threshold. Setting `random_state` to a fixed integer makes the results reproducible, while `predict()` returns `1` for inliers and `-1` for outliers. Lower values from `score_samples()` indicate more abnormal observations.

## Citation status

Read: Yes
Used in thesis: No
Reference checked: Yes

# Source S013

## Basic information

Author / Organization: Guilherme O. Campos, Arthur Zimek, Jörg Sander, Ricardo J. G. B. Campello, Barbora Micenková, Erich Schubert, Ira Assent, Michael E. Houle  
Year: 2016  
Title: On the evaluation of unsupervised outlier detection: measures, datasets, and an empirical study  
Source type: Peer-reviewed journal article  
Journal: Data Mining and Knowledge Discovery  
Volume: 30  
Issue: 4  
Pages: 891–927  
Publisher: Springer  
DOI: 10.1007/s10618-015-0444-8  

## Source access

University research record:
https://pure.au.dk/portal/en/publications/on-the-evaluation-of-unsupervised-outlier-detection-measures-data/

DOI:
https://doi.org/10.1007/s10618-015-0444-8

Open-access repository record:
https://repositorio.usp.br/item/002742759

Accessed:
21 October 2026

## Thesis topic

Relevant section:
- Knowledge Base
- Unsupervised anomaly detection
- Evaluation of anomaly-detection methods
- Statistical baseline vs Isolation Forest
- Limitations of the analysis

## What this source supports

- Evaluating unsupervised outlier-detection methods is challenging.
- Suitable datasets with reliable ground-truth labels are often difficult to obtain.
- Even when labelled datasets are available, they may not always be suitable for evaluating outlier detection.
- Parameter choices can affect the results of anomaly-detection algorithms.
- Different evaluation measures can produce different conclusions.
- Evaluation should therefore consider the characteristics of the dataset, the algorithm, and the selected evaluation method.

## Why this source is relevant to the thesis

The historical iSign CI/CD data does not contain predefined labels showing which workflow runs are truly normal or anomalous.

Therefore, the thesis cannot simply treat Isolation Forest results as automatically correct. The results need to be compared with the statistical baseline and investigated using the actual workflow and step-level data.

This source supports explaining this limitation and the need for careful evaluation of the detected anomalies.

## My understanding

Evaluating unsupervised outlier-detection methods is difficult because there is limited knowledge about the strengths and weaknesses of different models, and the effect of parameter choices is not always clear. A major problem is that benchmark datasets with reliable ground-truth labels are rare, and even when labelled data is available, it may not be suitable for outlier detection. The paper also explains that commonly used evaluation measures can have their own biases, which makes it difficult to know whether a new method really performs better than existing ones. To study this problem, the authors carried out a large experimental study using k-nearest-neighbour-based methods across many datasets and suggested more suitable ways to evaluate the results.

## Citation status

Read: Yes  
Used in thesis: No  
Reference checked: Yes

# Source S014

## Basic information

Author / Organization: NIST / SEMATECH
Year: n.d.
Title: Experimental Design
Source type: Official statistical handbook / technical web resource
Publisher: National Institute of Standards and Technology (NIST)

## Source access

What is experimental design?
https://www.itl.nist.gov/div898/handbook/pri/section1/pri11.htm

Steps of experimental design:
https://www.itl.nist.gov/div898/handbook/pri/section1/pri14.htm

Selecting an experimental design:
https://www.itl.nist.gov/div898/handbook/pri/section3/pri33.htm

One-factor experimental design:
https://www.itl.nist.gov/div898/handbook/pri/section3/pri331.htm

Accessed:
21 October 2026

## Thesis topic

Relevant section:
- Data and Methods
- Experimental evaluation
- Before/after comparison
- Performance measurement
- CI/CD optimization evaluation
- RQ3

## What this source supports

- An experiment deliberately changes one or more factors and measures the effect on one or more response variables.
- The objective of the experiment should be defined before measurements are collected.
- Process variables and response variables should be selected clearly.
- A comparative experiment can be used when the main goal is to study the effect of one important factor.
- When one main factor is being investigated, measurements can be compared across different levels of that factor.
- Several experimental runs are more useful than relying on only one measurement.
- Unexpected changes and process drift should be considered during an experiment.
- Raw measurement data should be preserved and important events should be recorded.
- Results should be analysed and interpreted after the experiment.

## Why this source is relevant to the thesis

The thesis will implement one evidence-based change to the selected iSign CI/CD workflow and measure its effect.

The workflow configuration is the main factor being changed, while metrics such as workflow execution time, job duration, and relevant step duration can be treated as response variables.

The source supports using several comparable measurements before and after the optimization instead of judging the result from only one workflow run. It also supports keeping other conditions as consistent as reasonably possible and recording changes that could affect the measurements.

## My understanding

A designed experiment is a planned activity in which one or more factors are changed on purpose so that their effect on one or more response variables can be observed. The objective of the experiment and the factors should be decided before any measurements are collected, and when one main factor is studied, the results can be compared across different levels of that factor. It is also better to carry out several experimental runs than to depend on only one measurement, and possible unexpected changes or process drift should be considered. Finally, the raw data should be kept, important events should be recorded, and the results should be analysed and interpreted carefully after the experiment.

## Citation status

Read: Yes
Used in thesis: No
Reference checked: Yes