import pandas as pd
import numpy as np
from scipy import stats

csv = r"C:\iSign_i3Cubes_Project\Thesis\data\processed\chapter7_vitest_main_14x14.csv"
df = pd.read_csv(csv)

metrics = {
    "Workflow duration": "WorkflowDuration_s",
    "Resource-use proxy": "AggregateJobTime_s",
    "SCP-related duration": "SCP_Total_s",
}

rows = []

for name, column in metrics.items():
    docker = df.loc[df["Method"] == "Docker", column].astype(float).to_numpy()
    native = df.loc[df["Method"] == "Native", column].astype(float).to_numpy()

    docker_mean = docker.mean()
    native_mean = native.mean()
    difference = native_mean - docker_mean
    reduction = ((docker_mean - native_mean) / docker_mean) * 100

    t_stat, p_value = stats.ttest_ind(native, docker, equal_var=False)

    var_n = native.var(ddof=1)
    var_d = docker.var(ddof=1)
    n_n = len(native)
    n_d = len(docker)

    se = np.sqrt(var_n / n_n + var_d / n_d)
    df_welch = (var_n / n_n + var_d / n_d) ** 2 / (
        ((var_n / n_n) ** 2 / (n_n - 1)) +
        ((var_d / n_d) ** 2 / (n_d - 1))
    )

    critical = stats.t.ppf(0.975, df_welch)
    ci_low = difference - critical * se
    ci_high = difference + critical * se

    rows.append({
        "Metric": name,
        "Docker_mean_s": round(docker_mean, 2),
        "Native_mean_s": round(native_mean, 2),
        "Native_minus_Docker_s": round(difference, 2),
        "Native_reduction_pct": round(reduction, 2),
        "Welch_t": round(t_stat, 3),
        "Welch_df": round(df_welch, 2),
        "p_value": round(p_value, 4),
        "CI95_low_s": round(ci_low, 2),
        "CI95_high_s": round(ci_high, 2),
    })

result = pd.DataFrame(rows)

output = r"C:\iSign_i3Cubes_Project\Thesis\data\processed\chapter7_vitest_main_14x14_welch.csv"
result.to_csv(output, index=False)

print(result.to_string(index=False))
print()
print("Saved:", output)
