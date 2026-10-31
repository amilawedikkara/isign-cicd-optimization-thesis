from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

input_path = Path("data/processed/isign_frontend_common_feature_method_comparison.csv")
output_path = Path("report/figures/iqr_vs_isolation_forest_comparison.png")

df = pd.read_csv(input_path)
order = ["both", "iqr_only", "isolation_forest_only", "normal_both"]
labels = ["Both methods", "IQR only", "Isolation Forest only", "Normal by both"]
counts = df["comparison_group"].value_counts().reindex(order, fill_value=0)

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.bar(labels, counts.values)
ax.set_ylabel("Number of workflow runs")
ax.set_xlabel("Classification")
ax.set_title("IQR and Isolation Forest Classification Comparison")
ax.set_ylim(0, max(counts.values) + 4)

for bar, value in zip(bars, counts.values):
    ax.text(bar.get_x() + bar.get_width()/2, value + 0.3, str(int(value)),
            ha="center", va="bottom")

fig.tight_layout()
fig.savefig(output_path, dpi=200)
plt.close(fig)

print("Figure 3 regenerated")
print(counts.to_string())
print(f"Saved: {output_path}")
