import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv = Path(r"C:\iSign_i3Cubes_Project\Thesis\data\processed\chapter7_no_vitest_combined_7sets.csv")
output = Path(r"C:\iSign_i3Cubes_Project\Thesis\report\figures\chapter7_no_vitest_scp_pairs.png")
output.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv)

docker = (
    df[df["Method"] == "Docker"]
    .sort_values("Set")["SCPRelatedTotal_s"]
    .astype(float)
    .to_numpy()
)

native = (
    df[df["Method"] == "Native"]
    .sort_values("Set")["SCPRelatedTotal_s"]
    .astype(float)
    .to_numpy()
)

pairs = list(range(1, 8))

fig, ax = plt.subplots(figsize=(9, 5.5))

ax.plot(pairs, docker, marker="o", label="Docker SCP")
ax.plot(pairs, native, marker="o", label="Native SCP")

ax.set_xlabel("Diagnostic run pair")
ax.set_ylabel("SCP-related duration (seconds)")
ax.set_title("SCP-related duration in the no-Vitest diagnostic runs")
ax.set_xticks(pairs)
ax.legend()
ax.grid(axis="y", alpha=0.25)

fig.tight_layout()
fig.savefig(output, dpi=300, bbox_inches="tight")
plt.close(fig)

print("Pair  Docker  Native  Native-Docker")
for pair, d, n in zip(pairs, docker, native):
    print(f"{pair:>4}  {d:>6.0f}  {n:>6.0f}  {n-d:>13.0f}")

print()
print(f"Docker mean: {docker.mean():.2f} s")
print(f"Native mean: {native.mean():.2f} s")
print("Saved:", output)
