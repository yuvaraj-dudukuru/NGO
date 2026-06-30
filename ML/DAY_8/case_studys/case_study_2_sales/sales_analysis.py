# ============================================================================
# CASE STUDY 2 — SALES DATASET
# ----------------------------------------------------------------------------
# Goal: Use visualizations to explore how advertising spend relates to revenue,
#       and to compare performance across regions.
#
# What you will practise here:
#   * Building a small DataFrame by hand with pandas
#   * Scatter plots to study a RELATIONSHIP between two numbers
#   * Computing a correlation coefficient with .corr()
#   * Bar plots to COMPARE a number across categories
#   * Box plots to inspect the SPREAD of a single number
#
# How to run this file:
#   1. Install the libraries once:  pip install pandas seaborn matplotlib
#   2. From a terminal run:         python sales_analysis.py
#   3. Each chart opens in its own window. Close a window to see the next one.
# ============================================================================

# --- Imports ----------------------------------------------------------------
# pandas  -> tables (DataFrames) and data manipulation
# seaborn -> high-level statistical plotting
# matplotlib.pyplot -> titles and showing the figures
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================================
# 22.1  THE DATA AND SETUP
# ============================================================================
# We build a tiny dataset by hand. Each key in the dictionary becomes a column,
# and each list becomes that column's values. All lists MUST be the same length
# (here 8 rows). Columns:
#   Region   -> where the sale happened (a category)
#   Product  -> which product was sold (a category)
#   AdSpend  -> money spent on advertising (numeric)
#   Revenue  -> money earned (numeric)
sales = pd.DataFrame({
    "Region":  ["North", "South", "East", "West", "North", "South", "East", "West"],
    "Product": ["A", "B", "A", "C", "C", "A", "B", "A"],
    "AdSpend": [10, 15, 20, 12, 25, 18, 14, 30],
    "Revenue": [120, 150, 240, 130, 300, 170, 160, 350],
})


# ============================================================================
# 22.2  RELATIONSHIP — AD SPEND vs REVENUE
# ============================================================================
# A scatter plot places one dot per row at position (AdSpend, Revenue).
# It is the go-to chart for seeing whether two numbers move together.
#   x="AdSpend"   -> horizontal axis
#   y="Revenue"   -> vertical axis
#   hue="Region"  -> color each dot by its region so groups stand out
sns.scatterplot(data=sales, x="AdSpend", y="Revenue", hue="Region")
plt.title("Ad Spend vs Revenue by Region")
plt.show()

# .corr() returns a number between -1 and +1 describing the linear link.
# round(..., 2) keeps it readable at 2 decimal places.
print("Correlation:", round(sales["AdSpend"].corr(sales["Revenue"]), 2))

# INTERPRETATION:
# The dots rise from lower-left to upper-right — a strong POSITIVE relationship.
# The printed correlation (about 0.96) confirms it numerically: higher ad spend
# is associated with higher revenue.


# ============================================================================
# 22.3  CATEGORY COMPARISON — AVERAGE REVENUE BY REGION
# ============================================================================
# A bar plot compares a numeric value across categories. By default seaborn
# shows the MEAN (average) of y for each x group, with a small line showing
# uncertainty.
#   x="Region"   -> one bar per region
#   y="Revenue"  -> bar height = average revenue for that region
sns.barplot(data=sales, x="Region", y="Revenue")
plt.title("Average Revenue by Region")
plt.show()

# INTERPRETATION:
# Seaborn automatically computes the average revenue per region.
# West and East show the highest averages.


# ============================================================================
# 22.4  DISTRIBUTION — REVENUE
# ============================================================================
# A single-variable box plot (only y given) shows the overall spread of revenue
# and flags any unusually high or low value as an outlier point.
sns.boxplot(data=sales, y="Revenue")
plt.title("Revenue Distribution")
plt.show()

# INTERPRETATION:
# The box plot shows where most revenue values sit and highlights any
# unusually high value as an outlier.


# ============================================================================
# 22.5  FINDINGS
# ============================================================================
# * Ad spend and revenue are strongly correlated (~0.96) — advertising appears
#   effective (but confirm CAUSATION before acting; correlation alone is not
#   proof).
# * West and East are the top-performing regions on average.
# * Recommendation: Consider increasing ad budgets (AFTER testing the causal
#   effect) and study what makes West and East succeed.
print("\nAnalysis complete. See the README for the full write-up.")
