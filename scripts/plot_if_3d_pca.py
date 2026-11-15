import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load historical Isolation Forest result
df = pd.read_csv(
    r"data\processed\isign_frontend_isolation_forest_results.csv"
)

features = [
    "scp_action_setup_seconds",
    "setup_node_seconds",
    "install_dependencies_seconds",
    "build_react_seconds",
    "scp_transfer_seconds"
]

# Use all five timing features
X = df[features]

# Standardize because the features have different ranges
X_scaled = StandardScaler().fit_transform(X)

# Reduce 5 dimensions to 3 dimensions for visualization
pca = PCA(n_components=3)
X_3d = pca.fit_transform(X_scaled)

df["PC1"] = X_3d[:, 0]
df["PC2"] = X_3d[:, 1]
df["PC3"] = X_3d[:, 2]

normal = df[df["if_is_anomaly"] == False]
anomaly = df[df["if_is_anomaly"] == True]
run1 = df[df["run_number"] == 1]

fig = plt.figure(figsize=(11, 8))
ax = fig.add_subplot(111, projection="3d")

# Normal runs
ax.scatter(
    normal["PC1"],
    normal["PC2"],
    normal["PC3"],
    marker="o",
    alpha=0.65,
    label="Normal runs"
)

# Isolation Forest anomalies
ax.scatter(
    anomaly["PC1"],
    anomaly["PC2"],
    anomaly["PC3"],
    marker="^",
    s=80,
    label="Isolation Forest anomalies"
)

# Highlight Run 1
ax.scatter(
    run1["PC1"],
    run1["PC2"],
    run1["PC3"],
    marker="X",
    s=220,
    label="Run 1"
)

# Label anomaly run numbers
for _, row in anomaly.iterrows():
    ax.text(
        row["PC1"],
        row["PC2"],
        row["PC3"],
        f'Run {int(row["run_number"])}'
    )

ax.set_xlabel("Principal Component 1")
ax.set_ylabel("Principal Component 2")
ax.set_zlabel("Principal Component 3")

ax.set_title(
    "Historical iSign Runs - Isolation Forest\n"
    "3D PCA view of five workflow timing features"
)

ax.legend()

plt.tight_layout()

output = r"data\processed\isign_if_3d_pca.png"
plt.savefig(output, dpi=200)

print("Saved:", output)
print(
    "Explained variance:",
    pca.explained_variance_ratio_,
    "Total:",
    pca.explained_variance_ratio_.sum()
)

plt.show()
