import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv = Path(r"C:\iSign_i3Cubes_Project\Thesis\data\processed\chapter7_vitest_main_14x14.csv")
output = Path(r"C:\iSign_i3Cubes_Project\Thesis\report\figures\chapter7_scp_duration_pairs.png")
output.parent.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv)
df["RunId"] = df["RunId"].astype(str)

pairs = [
    ("42667383442", "42667852602"),
    ("42668347896", "42668596663"),
    ("42668834540", "42669057430"),
    ("42669303013", "42669558032"),
    ("42673561116", "42671095730"),
    ("42675427918", "42675653456"),
    ("42679517099", "42679270390"),
    ("42679825720", "42680130219"),
    ("42865229462", "42865589069"),
    ("42866317008", "42865962966"),
    ("43693626385", "43693779260"),
    ("43694113641", "43693953820"),
    ("43694275588", "43694451651"),
    ("43694750052", "43694603355"),
]

docker = []
native = []

for docker_id, native_id in pairs:
    d = df.loc[df["RunId"] == docker_id, "SCP_Total_s"]
    n = df.loc[df["RunId"] == native_id, "SCP_Total_s"]

    if len(d) != 1 or len(n) != 1:
        raise ValueError(f"Missing or duplicate run: Docker={docker_id}, Native={native_id}")

    docker.append(float(d.iloc[0]))
    native.append(float(n.iloc[0]))

x = list(range(1, 15))

fig, ax = plt.subplots(figsize=(10, 5.5))
ax.plot(x, docker, marker="o", label="Docker SCP")
ax.plot(x, native, marker="o", label="Native SCP")

ax.set_xlabel("Controlled run pair")
ax.set_ylabel("SCP-related duration (seconds)")
ax.set_title("SCP-related duration across the 14 controlled run pairs")
ax.set_xticks(x)
ax.legend()
ax.grid(axis="y", alpha=0.25)

fig.tight_layout()
fig.savefig(output, dpi=300, bbox_inches="tight")
plt.close(fig)

print("Pair  Docker  Native  Native-Docker")
for i, (d, n) in enumerate(zip(docker, native), start=1):
    print(f"{i:>4}  {d:>6.0f}  {n:>6.0f}  {n-d:>13.0f}")

print()
print("Saved:", output)
