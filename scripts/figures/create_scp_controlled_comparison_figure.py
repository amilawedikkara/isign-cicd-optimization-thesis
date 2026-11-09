import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from pathlib import Path

input_file = Path("data/processed/scp_controlled_10_vs_10.csv")
output_file = Path("report/figures/scp_controlled_10_vs_10_comparison.png")

df = pd.read_csv(input_file)

native = df.loc[df["Method"] == "Native", "SCP_Total"].astype(float).to_numpy()
docker = df.loc[df["Method"] == "Docker", "SCP_Total"].astype(float).to_numpy()

def mean_ci(values):
    mean = np.mean(values)
    se = stats.sem(values)
    margin = stats.t.ppf(0.975, len(values) - 1) * se
    return mean, mean - margin, mean + margin

native_mean, native_low, native_high = mean_ci(native)
docker_mean, docker_low, docker_high = mean_ci(docker)

fig, ax = plt.subplots(figsize=(8, 5))

native_x = 1 + np.linspace(-0.08, 0.08, len(native))
docker_x = 2 + np.linspace(-0.08, 0.08, len(docker))

ax.scatter(native_x, native, label="Native SCP runs")
ax.scatter(docker_x, docker, label="Docker SCP runs")

ax.errorbar(
    1,
    native_mean,
    yerr=[[native_mean - native_low], [native_high - native_mean]],
    fmt="o",
    capsize=6,
    markersize=8,
    label="Mean and 95% CI"
)

ax.errorbar(
    2,
    docker_mean,
    yerr=[[docker_mean - docker_low], [docker_high - docker_mean]],
    fmt="o",
    capsize=6,
    markersize=8
)

ax.set_xticks([1, 2])
ax.set_xticklabels(["Native SCP", "Docker SCP"])
ax.set_ylabel("SCP-related execution time (seconds)")
ax.set_title("Controlled SCP Comparison: 10 Runs per Method")
ax.grid(axis="y", alpha=0.25)

fig.tight_layout()
fig.savefig(output_file, dpi=300, bbox_inches="tight")

print(f"Saved figure to: {output_file}")
print(f"Native mean: {native_mean:.2f} s")
print(f"Native 95% CI: [{native_low:.2f}, {native_high:.2f}] s")
print(f"Docker mean: {docker_mean:.2f} s")
print(f"Docker 95% CI: [{docker_low:.2f}, {docker_high:.2f}] s")