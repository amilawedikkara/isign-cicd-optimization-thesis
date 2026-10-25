# 3 ISIGN STARTING SITUATION AND OWN CONTRIBUTION

## 3.1 iSign System and Development Environment

iSign is an attendance management system that was developed as a team software project. The system has a web frontend, backend services, a mobile application, a verification service and a PostgreSQL database. The frontend is built with React and Vite, and the backend uses Node.js, Express and TypeScript. The Android mobile application is developed with Kotlin and Jetpack Compose, and the attendance verification service uses Python and FastAPI. GitHub is used for source code management, and GitHub Actions is used to automate CI/CD activities.

The main parts of the iSign system communicate through REST APIs. The Android application and the web frontend communicate with the Node.js/Express backend, and the backend communicates with the Python/FastAPI verification service when attendance verification is needed. PostgreSQL is used to store application and attendance-related data. This design keeps the mobile application separate from the internal verification service and allows the backend to control the verification process.

## 3.2 Existing Frontend CI/CD Workflow

The iSign frontend repository uses a GitHub Actions workflow called `Deploy to Dev Apache Server`. This workflow runs when code is pushed to the `development` branch, and it can also be triggered manually. It uses Node.js 20 and runs on an Ubuntu runner provided by GitHub. The workflow has two main jobs: `check-commit-message` and `build-and-deploy`. The first job checks whether the latest commit message contains the word `Deploy`, and this result decides whether the deployment job will run.

When the deployment condition is met, the `build-and-deploy` job gets the source code, sets up Node.js, installs the project dependencies and builds the React application. After the build is ready, the workflow sends the build files to the development server using SCP and completes the deployment process on the server. The workflow also has a verification step to make sure the deployment was successful.

## 3.3 Starting Situation Before the Thesis Development

Before the thesis work started, the iSign frontend CI/CD workflow was already in regular use, but its past execution data had not been studied in a systematic way. The workflow produced data about runs, jobs and steps in GitHub Actions, but there was no dedicated process for finding unusually slow runs, recurring performance problems or possible inefficiencies. Because of this, decisions about how to optimize the workflow were not based on a structured analysis of historical CI/CD data.

The available historical data showed that the frontend repository had 55 GitHub Actions workflow runs in the selected period. After filtering the data to keep comparable successful full executions, 33 runs remained for the main analysis. These runs contained 495 step-level observations. This cleaned dataset was used as the baseline for analysing workflow duration, job duration and the execution time of important workflow steps.

## 3.4 Own Contribution and Thesis Work Boundary

Before I started this thesis, I had already taken part in the development of the iSign system as a member of the project team. My earlier work included mobile application development, backend functionality, parts of the attendance verification service, API-related work and frontend integration tasks. These development tasks gave me practical knowledge of the system and its architecture. However, this earlier project work is not considered part of the thesis development contribution.

The thesis work starts with a systematic analysis of the iSign CI/CD workflow. This includes collecting and preparing historical GitHub Actions data, making a simple statistical baseline, using Isolation Forest to find anomalies, and comparing the results of the two methods. After this analysis, one practical CI/CD optimization will be selected, implemented, and evaluated using repeated before-and-after measurements. These activities form the main development and evaluation work of the thesis.
