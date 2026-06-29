# =============================================================================
# MINI CHALLENGE — TrendMart Six-Month Visual Performance Report
# =============================================================================
# SCENARIO:
#   You are a junior data analyst at "TrendMart", a retail chain. Management wants
#   a visual report of the last six months so they can decide where to invest next.
#
# YOUR JOB (the requirements):
#   1. Analyze the dataset      -> head() and describe()
#   2. Create multiple charts   -> line, bar, histogram, scatter
#   3. Customize every chart     -> titles, axis labels, colors
#   4. Compare findings          -> read the charts together
#   5. Detect anomalies          -> find the outlier in the histogram
#   6. Present insights          -> at least 3 insights, each with a recommendation
#   7. Save a high-res PNG        -> dpi=300
#
# This script does all seven, then adds the optional STRETCH GOALS at the end.
# =============================================================================


# -----------------------------------------------------------------------------
# STEP 0: Import the libraries
# -----------------------------------------------------------------------------
# pandas            -> hold and summarise the data in a table (DataFrame)
# matplotlib.pyplot -> draw all the charts
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# STEP 1: Create / load the dataset
# -----------------------------------------------------------------------------
# In a real project this data would come from a cleaned CSV file. Here we build it
# directly so the example is self-contained. Each list is one column; all lists
# have 6 values (one per month), so every row lines up.
data = pd.DataFrame({
    "Month":      ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],  # the six months
    "Revenue":    [120, 150, 130, 200, 240, 300],              # revenue per month
    "AdSpend":    [10, 15, 12, 20, 25, 32],                    # advertising spend
    "Region":     ["North", "South", "North", "East", "South", "East"],  # region
    "OrderValue": [450, 700, 380, 1200, 820, 5000]             # value of an order
})


# =============================================================================
# REQUIREMENT 1: Analyze the dataset
# =============================================================================
# head()      -> shows the first few rows so we can confirm the data loaded right.
# describe()  -> gives summary statistics (count, mean, min, max, etc.) for the
#                numeric columns. .round(1) keeps the numbers easy to read.
print("=" * 60)
print("STEP 1 — INSPECT THE DATA")
print("=" * 60)
print("\nFirst rows (head):")
print(data.head())

print("\nSummary statistics (describe):")
print(data.describe().round(1))
print()


# =============================================================================
# REQUIREMENTS 2 & 3: Create and customize multiple charts (a 2x2 dashboard)
# =============================================================================
# plt.subplots(2, 2) makes a grid of 4 charts arranged in 2 rows and 2 columns.
# We reach each chart with two indexes: axes[row, column].
#   axes[0, 0] top-left     axes[0, 1] top-right
#   axes[1, 0] bottom-left  axes[1, 1] bottom-right
fig, axes = plt.subplots(2, 2, figsize=(14, 9))


# ---- CHART 1 (top-left): Line chart of Revenue over the six months ----------
# A LINE chart is the right choice for a value changing over TIME.
# marker="o" puts a dot on each month so individual points are easy to read.
axes[0, 0].plot(data["Month"], data["Revenue"], marker="o", color="blue")
axes[0, 0].set_title("Revenue Trend")     # title above the chart
axes[0, 0].set_xlabel("Month")            # x-axis label
axes[0, 0].set_ylabel("Revenue")          # y-axis label


# ---- CHART 2 (top-right): Bar chart of total Revenue by Region ---------------
# groupby("Region") gathers all rows of the same region together, and
# ["Revenue"].sum() adds up their revenue. Result: total revenue per region.
region_rev = data.groupby("Region")["Revenue"].sum()

# .index  -> the region names (used as bar labels)
# .values -> the total revenue numbers (used as bar heights)
axes[0, 1].bar(region_rev.index, region_rev.values, color="green")
axes[0, 1].set_title("Revenue by Region")
axes[0, 1].set_xlabel("Region")
axes[0, 1].set_ylabel("Total Revenue")


# ---- CHART 3 (bottom-left): Histogram of OrderValue -------------------------
# A HISTOGRAM groups numbers into bins (ranges) and counts how many fall in each.
# It reveals the SHAPE of the data and makes outliers obvious.
# bins=5 splits the order values into 5 ranges; edgecolor outlines each bar.
axes[1, 0].hist(data["OrderValue"], bins=5, color="purple", edgecolor="black")
axes[1, 0].set_title("Order Value Distribution")
axes[1, 0].set_xlabel("Order Value")
axes[1, 0].set_ylabel("Count")


# ---- CHART 4 (bottom-right): Scatter plot of AdSpend vs Revenue -------------
# A SCATTER plot draws one dot per month at (AdSpend, Revenue). If the dots rise
# from bottom-left to top-right, more ad spend goes with more revenue
# -> a positive relationship.
axes[1, 1].scatter(data["AdSpend"], data["Revenue"], color="darkred")
axes[1, 1].set_title("Ad Spend vs Revenue")
axes[1, 1].set_xlabel("Ad Spend")
axes[1, 1].set_ylabel("Revenue")


# =============================================================================
# REQUIREMENT 7: Save at least one chart as a high-resolution PNG
# =============================================================================
# tight_layout() spaces the four charts so titles/labels don't overlap.
plt.tight_layout()

# dpi=300 makes a high-resolution image suitable for reports/printing.
# bbox_inches="tight" trims extra whitespace around the figure.
plt.savefig("trendmart_dashboard.png", dpi=300, bbox_inches="tight")

# Open a window to view the dashboard (when running locally).
plt.show()


# =============================================================================
# REQUIREMENT 5 (numeric check): Confirm the AdSpend–Revenue relationship
# =============================================================================
# .corr() returns a correlation coefficient between -1 and +1.
#   close to +1 -> strong positive relationship
#   close to  0 -> little/no relationship
#   close to -1 -> strong negative relationship
correlation = round(data["AdSpend"].corr(data["Revenue"]), 2)
print("=" * 60)
print("STEP 5 — NUMERIC CHECK")
print("=" * 60)
print(f"AdSpend vs Revenue correlation: {correlation}")
print()


# =============================================================================
# REQUIREMENT 5 (anomaly detection): Identify the outlier in the histogram
# =============================================================================
# A simple, beginner-friendly rule: flag any order whose value is far above the
# typical range. Here we flag orders above 2000 (well beyond the usual <1000).
outliers = data[data["OrderValue"] > 2000]
print("=" * 60)
print("ANOMALY DETECTION — Order Value outliers (> 2000)")
print("=" * 60)
print(outliers[["Month", "Region", "OrderValue"]])
print()


# =============================================================================
# REQUIREMENTS 4 & 6: Compare findings and present insights + recommendations
# =============================================================================
print("=" * 60)
print("INSIGHTS & RECOMMENDATIONS")
print("=" * 60)

print("""
INSIGHT 1 — Revenue is growing steadily.
  Evidence : Line chart rises from 120 (Jan) to 300 (Jun).
  Recommend: Sustain the current growth strategy; it is clearly working.

INSIGHT 2 — East and South lead; North lags.
  Evidence : Bar chart shows East and South with the highest total revenue,
             while North trails behind.
  Recommend: Study what makes East/South succeed and replicate it in North.

INSIGHT 3 — One order of 5000 is a clear outlier.
  Evidence : Histogram shows most orders under 1000, but one sits far away at 5000.
  Recommend: Follow up with that high-value customer; understand and repeat it.

INSIGHT 4 (bonus) — Ad spend correlates strongly with revenue.
  Evidence : Scatter plot trends up-right; correlation is near +1.
  Recommend: Consider increasing ad spend — but run a small test first to check
             whether the effect is truly causal (correlation is not causation).
""")


# =============================================================================
# STRETCH GOALS (optional extras) — saved as separate figures
# =============================================================================

# ---- STRETCH 1: Pie chart of each region's share of total revenue -----------
# A PIE chart shows proportions of a whole. We reuse region_rev from Chart 2.
fig2, ax2 = plt.subplots(figsize=(6, 6))
ax2.pie(region_rev.values, labels=region_rev.index,
        autopct="%1.1f%%", startangle=90)   # autopct prints each slice's % share
ax2.set_title("Revenue Share by Region")
plt.tight_layout()
plt.savefig("trendmart_region_share.png", dpi=300, bbox_inches="tight")
plt.show()


# ---- STRETCH 2: Two lines (AdSpend & Revenue) on one chart ------------------
# Plotting both on the same axes lets us compare how they grow together.
# We add a legend so the reader knows which line is which.
fig3, ax3 = plt.subplots(figsize=(8, 5))
ax3.plot(data["Month"], data["Revenue"], marker="o", color="blue", label="Revenue")
ax3.plot(data["Month"], data["AdSpend"], marker="s", color="orange", label="Ad Spend")
ax3.set_title("Revenue vs Ad Spend Over Time")
ax3.set_xlabel("Month")
ax3.set_ylabel("Amount")
ax3.legend()   # show the labels defined above
plt.tight_layout()
plt.savefig("trendmart_revenue_vs_adspend.png", dpi=300, bbox_inches="tight")
plt.show()

print("Done. Saved images:")
print("  - trendmart_dashboard.png        (the 4-chart dashboard)")
print("  - trendmart_region_share.png     (stretch: pie chart)")
print("  - trendmart_revenue_vs_adspend.png (stretch: two-line comparison)")
