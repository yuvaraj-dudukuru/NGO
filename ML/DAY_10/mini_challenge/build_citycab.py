"""
================================================================================
CityCab — END-TO-END RIDE ANALYSIS  (Mini Project Challenge)
================================================================================
You are the lead junior analyst at "CityCab", a ride-hailing company. Management
hands you a messy export of recent rides and asks for a complete analysis.

Running this script reproduces the whole project and writes two deliverables:
    * citycab_clean.csv       (the clean dataset)
    * charts/*.png            (saved visualizations, dpi=300)
The Jupyter notebook (citycab_analysis.ipynb) holds the same code in cells.
================================================================================
"""

import os
import sqlite3
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

HERE = os.path.dirname(os.path.abspath(__file__))
CHARTS = os.path.join(HERE, "charts")
os.makedirs(CHARTS, exist_ok=True)

# ---- Raw messy export --------------------------------------------------------
rides = pd.DataFrame({
    "RideID":   [1, 2, 3, 3, 5, 6, 7, 8, 9, 10],
    "Driver":   ["  ravi", "ASHA", "imran", "imran", "Divya",
                 "KARAN", "meena ", "Sahil", "tara", "asha"],
    "City":     ["Pune", "mumbai", "Pune", "Pune", "Delhi",
                 "Mumbai", "delhi", "Pune", "Mumbai", "mumbai"],
    "Distance": [5.2, 12.0, 3.5, 3.5, 8.0, 2.1, -4.0, 15.0, 6.5, 200.0],
    "Fare":     [120, 300, np.nan, 90, 200, 60, 110, 380, 160, 5000],
    "RideDate": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02", "2026-05-03",
                 "2026-05-04", "2026-05-05", "2026-05-06", "2026-05-07", "2026-05-08"],
})

# ============================================================================
# STEP 1 — INSPECT  (Day 4)
# ============================================================================
print("=== STEP 1: INSPECT ===")
print(rides.head())
print("\nShape:", rides.shape)
print("\ndescribe():\n", rides.describe(), sep="")
print("""
Red flags: RideID 3 duplicated | Fare has 1 missing | Distance -4.0 (impossible)
| Distance 200.0 and Fare 5000 (extreme outliers) | mixed-case text | RideDate text.
""")

# ============================================================================
# STEP 2 — CLEAN  (Day 5)
# ============================================================================
print("=== STEP 2: CLEAN ===")
df = rides.copy()

# 2a. Duplicate RideID 3. NOTE: the two copies differ (one Fare is NaN), so a
#     full-row duplicated() check would MISS it -> we dedupe on the business key.
#     We keep the FIRST copy; its missing fare is then fixed in step 2e (this
#     mirrors the brief's separate 'missing fare' step). In a real project you
#     might instead keep the row that already has a known fare.
print("Duplicate RideIDs:", df.duplicated(subset=["RideID"]).sum())
df = df.drop_duplicates(subset=["RideID"]).reset_index(drop=True)

# 2b. Fix type: text -> datetime.
df["RideDate"] = pd.to_datetime(df["RideDate"])

# 2c. Standardize text.
df["Driver"] = df["Driver"].str.strip().str.title()
df["City"] = df["City"].str.strip().str.title()

# 2d. Invalid distance (-4.0) -> median of valid (positive) distances.
valid_dist_median = df.loc[df["Distance"] > 0, "Distance"].median()
df.loc[df["Distance"] <= 0, "Distance"] = valid_dist_median

# 2e. Outlier distance (200 km): inspect with IQR, treat as error -> median.
Q1d, Q3d = df["Distance"].quantile([0.25, 0.75])
upper_d = Q3d + 1.5 * (Q3d - Q1d)
print("Distance IQR upper fence:", round(upper_d, 2))
print("Distance outliers:\n", df[df["Distance"] > upper_d][["RideID", "Distance"]], sep="")
df.loc[df["Distance"] > upper_d, "Distance"] = np.nan
df["Distance"] = df["Distance"].fillna(df["Distance"].median())

# 2f. Outlier fare (5000) + missing fare: inspect with IQR, then median-fill both.
Q1f, Q3f = df["Fare"].quantile([0.25, 0.75])
upper_f = Q3f + 1.5 * (Q3f - Q1f)
print("Fare IQR upper fence:", round(upper_f, 2))
print("Fare outliers:\n", df[df["Fare"] > upper_f][["RideID", "Fare"]], sep="")
df.loc[df["Fare"] > upper_f, "Fare"] = np.nan
df["Fare"] = df["Fare"].fillna(df["Fare"].median())

# 2g. Validate.
assert df.isnull().sum().sum() == 0 and df.duplicated(subset=["RideID"]).sum() == 0
assert (df["Distance"] > 0).all() and (df["Fare"] > 0).all()
print("\nValidation passed. Clean shape:", df.shape)   # ~9 rides
print(df)
df.to_csv(os.path.join(HERE, "citycab_clean.csv"), index=False)
print("Saved citycab_clean.csv")

# ============================================================================
# STEP 3 — EXPLORE  (Day 6)
# ============================================================================
print("\n=== STEP 3: EXPLORE ===")
print("Average fare:", round(df["Fare"].mean(), 2))
print("Average distance:", round(df["Distance"].mean(), 2))
fare_by_city = df.groupby("City")["Fare"].sum().sort_values(ascending=False)
print("\nTotal fare by city:\n", fare_by_city, sep="")
corr = df["Distance"].corr(df["Fare"])
print("\nCorrelation (Distance vs Fare):", round(corr, 2))

# ============================================================================
# STEP 4 — VISUALIZE  (Day 7/8)
# ============================================================================
print("\n=== STEP 4: VISUALIZE ===")
sns.set_theme(style="whitegrid")


def save(name):
    plt.tight_layout(); plt.savefig(os.path.join(CHARTS, name), dpi=300); plt.close()


plt.figure(); sns.barplot(x=fare_by_city.index, y=fare_by_city.values)
plt.title("Total Fare by City"); plt.xlabel("City"); plt.ylabel("Total Fare (Rs.)")
save("01_fare_by_city.png")

plt.figure(); sns.histplot(df["Fare"], bins=6, kde=True)
plt.title("Distribution of Fares"); plt.xlabel("Fare (Rs.)"); plt.ylabel("Count")
save("02_fare_distribution.png")

plt.figure(); sns.boxplot(y=df["Fare"])
plt.title("Fare Spread (Box Plot)"); plt.ylabel("Fare (Rs.)")
save("03_fare_box.png")

plt.figure(); sns.scatterplot(data=df, x="Distance", y="Fare", hue="City", s=120)
plt.title("Distance vs Fare"); plt.xlabel("Distance (km)"); plt.ylabel("Fare (Rs.)")
save("04_distance_vs_fare.png")

plt.figure(); sns.heatmap(df[["Distance", "Fare"]].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
save("05_correlation_heatmap.png")
print("Saved 5 charts to charts/ (dpi=300)")

# ============================================================================
# STEP 5 — SQL  (Day 9)
# ============================================================================
print("\n=== STEP 5: SQL ===")
conn = sqlite3.connect(":memory:")
df.to_sql("rides", conn, index=False, if_exists="replace")
print("Q1 Total fare by city:\n",
      pd.read_sql("SELECT City, SUM(Fare) AS TotalFare FROM rides "
                  "GROUP BY City ORDER BY TotalFare DESC", conn), sep="")
print("\nQ2 Rides above Rs.150:\n",
      pd.read_sql("SELECT Driver, City, Fare FROM rides "
                  "WHERE Fare > 150 ORDER BY Fare DESC", conn), sep="")
print("\nQ3 Pune ride list:\n",
      pd.read_sql("SELECT Driver, Distance, Fare FROM rides WHERE City = 'Pune'", conn), sep="")
conn.close()

# ============================================================================
# STEP 6 — INSIGHTS (insight ladder)
# ============================================================================
print("\n=== STEP 6: INSIGHTS ===")
print(f"""
1. OBS: {fare_by_city.index[0]} has the highest total fare (Rs.{fare_by_city.iloc[0]:.0f}).
   FIND: It is the busiest / highest-earning market.
   INSIGHT: Demand is concentrated in {fare_by_city.index[0]}.
   RECOMMEND: Allocate more drivers to {fare_by_city.index[0]}, especially at peak times.

2. OBS: Distance and Fare are positively correlated (corr = {corr:.2f}).
   FIND: Longer rides cost more - the pricing model behaves as expected.
   INSIGHT: Fare scales with distance (intuitively causal, but still a correlation).
   RECOMMEND: Use the distance-fare line as a sanity check to flag mispriced rides.

3. OBS: A 200 km ride and a Rs.5000 fare appeared (both corrected).
   FIND: Impossible values reached the export.
   INSIGHT: Input validation at ride logging is weak.
   RECOMMEND: Add range checks (max distance, max fare) at data entry.
""")
print("DONE. Full written report in EDA_REPORT.md")
