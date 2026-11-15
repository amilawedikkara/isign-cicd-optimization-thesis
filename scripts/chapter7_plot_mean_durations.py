import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

csv = Path(r"C:\iSign_i3Cubes_Project\Thesis\data\processed\chapter7_vitest_main_14x14.csv")
output = Path(r"C:\iSign_i3Cubes_Project\Thesis\report\figures\chapter7_mean_durations.png")
output.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv)

metrics = [
    ("Workflow duration", "WorkflowDuration_s"),
    ("Resource-use proxy", "AggregateJobTime_s"),
    ("SCP-related duration", "SCP_Total_s"),
]

docker_means = []
native_means = []

for label, column in metrics:
    docker_means.append(df.loc[df["Method"] == "Docker", column].mean())
    native_means.append(df.loc[df["Method"] == "Native", column].mean())

labels = [m[0] for m in metrics]
x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5.5))

bars_d = ax.bar(x - width/2, docker_means, width, label="Docker SCP")
bars_n = ax.bar(x + width/2, native_means, width, label="Native SCP")

ax.set_ylabel("Mean duration (seconds)")
ax.set_title("Mean durations in the main Vitest-enabled evaluation")
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
ax.grid(axis="y", alpha=0.25)

for bars in (bars_d, bars_n):
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 1,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=9
        )

ax.set_ylim(0, max(max(docker_means), max(native_means)) * 1.18)
fig.tight_layout()
fig.savefig(output, dpi=300, bbox_inches="tight")
plt.close(fig)

print("Docker means:", [round(x, 2) for x in docker_means])
print("Native means:", [round(x, 2) for x in native_means])
print("Saved:", output)
