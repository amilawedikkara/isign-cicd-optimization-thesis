import pandas as pd
import numpy as np
from scipy import stats

csv = r"C:\iSign_i3Cubes_Project\Thesis\data\processed\chapter7_no_vitest_combined_7sets.csv"
df = pd.read_csv(csv)

docker = df[df["Method"] == "Docker"].sort_values("Set")
native = df[df["Method"] == "Native"].sort_values("Set")

d = docker["SCPRelatedTotal_s"].astype(float).to_numpy()
n = native["SCPRelatedTotal_s"].astype(float).to_numpy()
diff = n - d

d_mean = d.mean()
n_mean = n.mean()
reduction = ((d_mean - n_mean) / d_mean) * 100

paired_t, paired_p = stats.ttest_rel(n, d)

diff_mean = diff.mean()
diff_sd = diff.std(ddof=1)
se = diff_sd / np.sqrt(len(diff))
critical = stats.t.ppf(0.975, len(diff) - 1)
paired_ci_low = diff_mean - critical * se
paired_ci_high = diff_mean + critical * se

welch_t, welch_p = stats.ttest_ind(n, d, equal_var=False)

var_n = n.var(ddof=1)
var_d = d.var(ddof=1)
n_n = len(n)
n_d = len(d)

welch_se = np.sqrt(var_n/n_n + var_d/n_d)
welch_df = (var_n/n_n + var_d/n_d)**2 / (
    ((var_n/n_n)**2/(n_n-1)) + ((var_d/n_d)**2/(n_d-1))
)
welch_critical = stats.t.ppf(0.975, welch_df)
welch_diff = n_mean - d_mean
welch_ci_low = welch_diff - welch_critical * welch_se
welch_ci_high = welch_diff + welch_critical * welch_se

print("=== 7x7 NO-VITEST DIAGNOSTIC ===")
print(f"Docker mean: {d_mean:.2f} s")
print(f"Native mean: {n_mean:.2f} s")
print(f"Difference Native-Docker: {diff_mean:.2f} s")
print(f"Native reduction: {reduction:.2f}%")
print()
print(f"Docker median: {np.median(d):.2f} s")
print(f"Native median: {np.median(n):.2f} s")
print(f"Docker SD: {d.std(ddof=1):.2f} s")
print(f"Native SD: {n.std(ddof=1):.2f} s")
print()
print("Paired differences:", diff.tolist())
print(f"Paired t = {paired_t:.3f}")
print(f"Paired p = {paired_p:.4f}")
print(f"Paired 95% CI = [{paired_ci_low:.2f}, {paired_ci_high:.2f}] s")
print()
print(f"Welch t = {welch_t:.3f}")
print(f"Welch df = {welch_df:.2f}")
print(f"Welch p = {welch_p:.4f}")
print(f"Welch 95% CI = [{welch_ci_low:.2f}, {welch_ci_high:.2f}] s")

result = pd.DataFrame([{
    "Docker_mean_s": round(d_mean,2),
    "Native_mean_s": round(n_mean,2),
    "Native_minus_Docker_s": round(diff_mean,2),
    "Native_reduction_pct": round(reduction,2),
    "Paired_t": round(paired_t,3),
    "Paired_p": round(paired_p,4),
    "Paired_CI95_low_s": round(paired_ci_low,2),
    "Paired_CI95_high_s": round(paired_ci_high,2),
    "Welch_t": round(welch_t,3),
    "Welch_df": round(welch_df,2),
    "Welch_p": round(welch_p,4),
    "Welch_CI95_low_s": round(welch_ci_low,2),
    "Welch_CI95_high_s": round(welch_ci_high,2)
}])

output = r"C:\iSign_i3Cubes_Project\Thesis\data\processed\chapter7_no_vitest_combined_7sets_stats.csv"
result.to_csv(output, index=False)
print()
print("Saved:", output)
