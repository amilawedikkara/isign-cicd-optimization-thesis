import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path

input_file = Path("data/processed/scp_controlled_10_vs_10.csv")
output_file = Path("data/processed/scp_controlled_10_vs_10_statistics.csv")

df = pd.read_csv(input_file)

native = df.loc[df["Method"] == "Native", "SCP_Total"].astype(float).to_numpy()
docker = df.loc[df["Method"] == "Docker", "SCP_Total"].astype(float).to_numpy()

def summary(values):
    return {
        "n": len(values),
        "mean": np.mean(values),
        "median": np.median(values),
        "std": np.std(values, ddof=1),
        "min": np.min(values),
        "max": np.max(values),
        "range": np.max(values) - np.min(values),
    }

native_stats = summary(native)
docker_stats = summary(docker)

mean_difference = native.mean() - docker.mean()
percentage_reduction = ((docker.mean() - native.mean()) / docker.mean()) * 100

# Welch's two-sample t-test
test = stats.ttest_ind(native, docker, equal_var=False)

# Welch-Satterthwaite degrees of freedom
n1, n2 = len(native), len(docker)
v1, v2 = np.var(native, ddof=1), np.var(docker, ddof=1)

se = np.sqrt(v1 / n1 + v2 / n2)

df_welch = (
    (v1 / n1 + v2 / n2) ** 2
    /
    (
        ((v1 / n1) ** 2 / (n1 - 1))
        +
        ((v2 / n2) ** 2 / (n2 - 1))
    )
)

critical = stats.t.ppf(0.975, df_welch)

ci_lower = mean_difference - critical * se
ci_upper = mean_difference + critical * se

success_native = (
    (df["Method"].eq("Native")) &
    (df["Conclusion"].eq("success"))
).sum()

success_docker = (
    (df["Method"].eq("Docker")) &
    (df["Conclusion"].eq("success"))
).sum()

results = pd.DataFrame([
    {
        "Metric": "Runs",
        "Native": native_stats["n"],
        "Docker": docker_stats["n"]
    },
    {
        "Metric": "Mean_seconds",
        "Native": native_stats["mean"],
        "Docker": docker_stats["mean"]
    },
    {
        "Metric": "Median_seconds",
        "Native": native_stats["median"],
        "Docker": docker_stats["median"]
    },
    {
        "Metric": "SD_seconds",
        "Native": native_stats["std"],
        "Docker": docker_stats["std"]
    },
    {
        "Metric": "Minimum_seconds",
        "Native": native_stats["min"],
        "Docker": docker_stats["min"]
    },
    {
        "Metric": "Maximum_seconds",
        "Native": native_stats["max"],
        "Docker": docker_stats["max"]
    },
    {
        "Metric": "Range_seconds",
        "Native": native_stats["range"],
        "Docker": docker_stats["range"]
    },
    {
        "Metric": "Successful_runs",
        "Native": success_native,
        "Docker": success_docker
    }
])

results.to_csv(output_file, index=False)

print("\n=== DESCRIPTIVE STATISTICS ===")
print(results.to_string(index=False))

print("\n=== COMPARISON ===")
print(f"Mean difference (Native - Docker): {mean_difference:.2f} s")
print(f"Percentage reduction: {percentage_reduction:.2f}%")

print("\n=== WELCH T-TEST ===")
print(f"t statistic: {test.statistic:.4f}")
print(f"degrees of freedom: {df_welch:.4f}")
print(f"p value: {test.pvalue:.8f}")
print(
    f"95% CI for mean difference: "
    f"[{ci_lower:.2f}, {ci_upper:.2f}] s"
)

print(f"\nSaved statistics to: {output_file}")