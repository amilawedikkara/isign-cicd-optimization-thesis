# Thesis Meeting 3 – Chapter 5 Results and Chapter 6 Progress

## 1. Current thesis status

### Chapter 5 – iSign Analysis Results

**Status: approximately 95–100% complete**

The technical analysis for Chapter 5 is complete. One open point is whether the current IQR method is enough as the simple statistical baseline.

### Completed work

The original iSign frontend dataset contained **55 GitHub Actions workflow runs**.

After applying the comparison rules:

- 22 runs were excluded (they did not complete the same full successful workflow)
- 33 successful and comparable runs were kept
- 495 step-level observations were analysed

The analysis included:

- descriptive statistics
- overall IQR analysis
- common-feature IQR analysis
- Isolation Forest analysis
- comparison between IQR and Isolation Forest
- numerical checking of the flagged runs

The same five timing features were used for the IQR and Isolation Forest comparison:

1. SCP action setup
2. Node.js setup
3. dependency installation
4. React build
5. SCP transfer

### IQR vs Isolation Forest results

IQR checks each timing feature separately and shows when one step has an unusually high or low duration. Isolation Forest looks at all five timing features together as one pattern for each workflow run. Because of this, Isolation Forest can identify a run as unusual even when none of the individual timing values is outside the IQR limits.

Among the 33 comparable runs:

- 7 runs were flagged by both methods (Runs 2, 3, 19, 37, 39, 52 and 55)
- 3 runs were flagged only by IQR (Runs 4, 22 and 38)
- 1 run was flagged only by Isolation Forest (Run 1)
- 22 runs were classified as normal by both methods

This comparison mainly supports **RQ2** because it shows how Isolation Forest performs compared with a simple statistical method.

The results also support **RQ1** because they identify unusual workflow behaviour that needs further technical investigation.

Chapter 5 identifies unusual timing behaviour.

---

## 2. Chapter 6 – Technical Investigation and Optimization Selection

Chapter 6 investigates whether the unusual results found in Chapter 5 have a real technical cause that can be improved.

**Current status: approximately 65–75% complete**

The final optimization has **not yet been selected**.

At the moment, the SCP deployment stage is the main candidate because Chapter 5 found several unusual SCP setup and transfer times.

### Technical investigation completed so far

The workflow configuration and available GitHub Actions logs were checked.

Several unusual SCP setup times were confirmed.

For example:

- Run 55 had an SCP action setup time of 14 seconds
- Run 39 had an SCP action setup time of 11 seconds
- Run 37 had an SCP action setup time of 10 seconds
- Run 22 had an SCP action setup time of 9 seconds

The IQR upper limit for SCP action setup was 8 seconds.

Across the 33 comparable historical runs:

- minimum SCP setup time: 2 seconds
- average SCP setup time: about 5 seconds
- maximum SCP setup time: 14 seconds

This shows that the Docker-based SCP action needs setup work in every deployment run. In some runs, this setup time was unusually high.

However, this does **not yet prove that Docker SCP is inefficient**.

---

## 3. Investigation of SCP transfer behaviour

Historical logs were checked when they were available.

The comparison between normal and unusual runs showed that the actual file transfer could sometimes take a similar time even when the Docker setup time was higher.

Run 52 showed a different case. Its SCP transfer was much slower, even though the frontend build size was not larger than in a normal comparison run.

This means that some slow SCP transfers may be caused by temporary network or server conditions instead of the workflow design.

Because of this, controlled testing is needed before choosing the final optimization.

---

## 4. Checking whether Native SCP can be used

A simpler deployment method was tested as an alternative.

The GitHub-hosted runner was confirmed to have:

- `ssh`
- `scp`
- `sshpass`

This means that the runner can transfer files directly without starting a separate Docker-based SCP action.

A temporary test branch was created, and the Docker-based SCP step was replaced with native SCP.

The application code and the rest of the server deployment process were kept the same.

---

## 5. Controlled Docker vs Native SCP experiment

Controlled tests were carried out for both methods.

Both methods completed the deployment successfully.

Current test data:

- 12 controlled Docker-SCP runs
- 12 controlled native-SCP runs

### Current SCP timing results

| Metric                 | Docker SCP | Native SCP |
| ---------------------- | ---------- | ---------- |
| Runs                   | 12         | 12         |
| Mean                   | 27.92 s    | 25.75 s    |
| Median                 | 29 s       | 20 s       |
| Minimum                | 22 s       | 18 s       |
| Maximum                | 37 s       | 83 s       |
| Successful deployments | 12/12      | 12/12      |

Native SCP was faster in most runs, especially when the median values are compared.

However, one native SCP run took **83 seconds**.

Because of this very slow run, native SCP cannot yet be selected as the final optimization.

---

## 6. Investigation of the 83-second Native SCP run

The slow native SCP run was checked in more detail.

The full delay happened inside the native SCP deployment step.

The `ssh-keyscan` part behaved normally and took about the same time as in a normal native SCP run.

The remaining delay happened during one of these two operations:

- creating the remote deployment folder through SSH
- transferring the files using SCP

The current workflow logs do not show the time for these two operations separately.

Because of this, more detailed timing measurements are needed to find the exact cause.

---

## 7. Current conclusion

The investigation has followed this path:

**Historical anomaly detection**\
**→ unusual SCP behaviour found**\
**→ workflow and logs checked**\
**→ Docker setup overhead identified**\
**→ native SCP tested as an alternative**\
**→ controlled Docker and native SCP runs compared**\
**→ native SCP was faster in most runs**\
**→ one very slow native SCP run still needs investigation**

The final optimization has **not yet been selected**.

Native SCP is still the strongest current candidate. However, it should only be selected if the remaining investigation shows that it gives a reliable and useful improvement.

If native SCP does not give a reliable improvement, the next step will be to investigate another optimization candidate that is supported by the workflow data.

---

## 8. Questions for Jukka

1. Is the current common-feature IQR analysis enough as the simple statistical baseline for RQ2, or should another simple statistical method also be used?
2. Is the controlled Docker-SCP vs native-SCP experiment a suitable way to support the optimization selection?
3. For the final performance evaluation, is it enough to report repeated measurements, mean, median, standard deviation, percentage improvement and a 95% confidence interval, with a permutation test as additional statistical evidence?

---

## 9. Planned work for next week

1. Add separate timing measurements for:
   - `ssh-keyscan`
   - remote SSH folder creation
   - actual SCP file transfer
2. Investigate the reason for the 83-second native SCP run.
3. Complete the controlled Docker-SCP vs native-SCP comparison.
4. Calculate:
   - mean
   - median
   - standard deviation
   - range
   - percentage difference
   - 95% confidence interval
   - optional permutation-test result
5. Decide whether native SCP can be selected as the final evidence-based optimization.
6. If native SCP is not reliable enough, investigate the next optimization candidate supported by the data.
7. Complete the remaining parts of Chapter 6 after the optimization decision.
8. After Chapter 6 is complete, prepare the formal before-and-after evaluation for Chapter 7.