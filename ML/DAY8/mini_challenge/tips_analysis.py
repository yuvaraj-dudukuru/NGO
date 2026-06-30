# ============================================================================
# MINI CHALLENGE — "DineWell" RESTAURANT: WHAT DRIVES BILLS AND TIPS?
# ----------------------------------------------------------------------------
# Scenario: You are a junior data analyst at "DineWell", a restaurant chain.
#           Management wants to understand what drives bills and tips so they
#           can boost revenue. You will use Seaborn to perform a complete
#           statistical visualization analysis of the classic "tips" dataset
#           and present business insights.
#
# What you will practise here:
#   * Inspecting a dataset (head, describe, missing values)
#   * Distribution, box, violin, scatter, count and bar plots
#   * A correlation heatmap
#   * Turning charts into BUSINESS insights + recommendations
#   * Optional stretch goals: hue box plot, pair plot, EDA report
#
# How to run this file:
#   1. Install the libraries once:  pip install numpy pandas matplotlib seaborn
#   2. From a terminal run:          python tips_analysis.py
#   3. Each chart opens in its own window. Close a window to see the next one.
# ============================================================================

# --- Imports ----------------------------------------------------------------
# numpy   -> numerical helpers (imported as the brief requests; handy for math)
# pandas  -> tables (DataFrames) and data manipulation
# matplotlib.pyplot -> titles and showing the figures
# seaborn -> high-level statistical plotting
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# set_theme applies a clean, consistent look to every chart.
# style="whitegrid" draws light horizontal grid lines that make values easy
# to read off the axes.
sns.set_theme(style="whitegrid")

# The "tips" dataset is built into seaborn, so no CSV download is needed.
# Columns:
#   total_bill -> the bill amount in dollars (numeric)
#   tip        -> the tip amount in dollars (numeric)
#   sex        -> gender of the bill payer (category)
#   smoker     -> whether the party included smokers (category)
#   day        -> day of the week (Thur/Fri/Sat/Sun)
#   time       -> Lunch or Dinner (category)
#   size       -> number of people in the party (numeric)
tips = sns.load_dataset("tips")


# ============================================================================
# 1. ANALYZE THE DATASET  (inspect before you visualize — Days 4-6 habit)
# ============================================================================
# .head() shows the first 5 rows so we can see the columns and example values.
print("First 5 rows:")
print(tips.head())

# .describe() gives summary statistics (count, mean, std, min, quartiles, max)
# for every NUMERIC column. Great for spotting the typical range and extremes.
print("\nSummary statistics:")
print(tips.describe())

# .isnull().sum() counts missing values per column. Here it should be all zeros
# (the tips dataset is clean), but checking is a non-negotiable habit.
print("\nMissing values per column:")
print(tips.isnull().sum())


# ============================================================================
# 2. STATISTICAL VISUALIZATIONS
# ============================================================================

# --- 2a. Distribution of total_bill (histogram + KDE) -----------------------
# A histogram shows how a single numeric column is spread out.
#   bins=20  -> split the bill range into 20 bars
#   kde=True -> overlay a smooth density curve
sns.histplot(data=tips, x="total_bill", bins=20, kde=True)
plt.title("Distribution of Total Bill")
plt.show()
# INTERPRETATION: total_bill is RIGHT-SKEWED — most bills are small, with a
# long tail of a few large bills.

# --- 2b. Box plot of total_bill by day --------------------------------------
# Compares the bill distribution across days and flags outliers as dots.
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill by Day")
plt.show()
# INTERPRETATION: Weekends (Sat/Sun) tend to show higher bills and more
# high-value outliers than weekdays.

# --- 2c. Violin plot of total_bill by time ----------------------------------
# A violin plot is a box plot + a mirrored density curve. The WIDTH at any
# height shows how many bills sit near that value.
sns.violinplot(data=tips, x="time", y="total_bill")
plt.title("Bill Distribution by Meal Time")
plt.show()
# INTERPRETATION: Dinner bills tend to be larger and more spread out than
# Lunch bills.

# --- 2d. Scatter plot of total_bill vs tip, colored by time -----------------
# One dot per bill at position (total_bill, tip), colored by meal time.
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time")
plt.title("Bill vs Tip by Meal Time")
plt.show()
# INTERPRETATION: Dots rise from lower-left to upper-right — bigger bills bring
# bigger tips (a strong positive relationship).

# --- 2e. Count plot of records per day --------------------------------------
# Counts how many bills were recorded on each day (how busy the day was).
sns.countplot(data=tips, x="day")
plt.title("Records per Day")
plt.show()
# INTERPRETATION: Saturday is typically the busiest day (most records).

# --- 2f. Bar plot of average bill per day -----------------------------------
# By default seaborn shows the MEAN bill for each day.
sns.barplot(data=tips, x="day", y="total_bill")
plt.title("Average Bill per Day")
plt.show()
# INTERPRETATION: Average bills peak on certain days (often Sun/Sat).


# ============================================================================
# 3. CORRELATION STUDY
# ============================================================================
# Correlation measures how strongly two numeric columns move together,
# from -1 (opposite) through 0 (no link) to +1 (together).
#   numeric_only=True -> skip text columns; correlation needs numbers
corr = tips.corr(numeric_only=True)

# Visualize the correlation table as an annotated heatmap.
#   annot=True      -> print the number in each cell
#   cmap="coolwarm" -> blue = negative, red = positive
#   fmt=".2f"       -> 2 decimal places
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
# Print the strongest pair for the report.
print("\nCorrelation between total_bill and tip:",
      round(tips["total_bill"].corr(tips["tip"]), 2))
# INTERPRETATION: total_bill and tip are strongly positively correlated
# (~0.68) — bigger bills bring bigger tips. size also correlates with the bill.


# ============================================================================
# 4. TRENDS AND OUTLIERS (summary of what the charts revealed)
# ============================================================================
# * Distribution shape : total_bill is RIGHT-SKEWED (most bills small, a few large).
# * Strongest correlation : total_bill <-> tip (~0.68).
# * Outliers : the box plot shows high-value outliers, mostly on weekends.


# ============================================================================
# 5. BUSINESS INSIGHTS + RECOMMENDATIONS
# ============================================================================
# Insight 1: Bigger bills directly produce bigger tips (~0.68 correlation).
#   -> Recommendation: Train staff on UPSELLING (sides, drinks, desserts);
#      higher bills raise revenue AND tips at the same time.
#
# Insight 2: Dinners and weekends bring the largest bills (violin + box plots).
#   -> Recommendation: Focus PREMIUM menus and promotions on dinner service and
#      weekends, when guests already spend more.
#
# Insight 3: Party size moves with the bill, and Saturday is busiest.
#   -> Recommendation: Encourage LARGER parties (group offers, set menus) and
#      schedule the best staff on Saturdays to capture peak demand.
print("\nAnalysis complete. See the README for the full business report.")


# ============================================================================
# STRETCH GOALS (optional) — uncomment any block to explore further
# ============================================================================

# --- Stretch 1: Box plot of bill by day, split by sex -----------------------
# Adding hue="sex" draws side-by-side boxes for male vs female per day.
# sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")
# plt.title("Total Bill by Day and Sex")
# plt.show()

# --- Stretch 2: Pair plot of total_bill, tip and size, colored by time ------
# A pair plot draws a scatter for every pair of the chosen numeric columns
# (and a distribution on the diagonal), revealing all relationships at once.
# sns.pairplot(tips[["total_bill", "tip", "size", "time"]], hue="time")
# plt.show()

# --- Stretch 3: Mini EDA report (printed text, Day 6 template) ---------------
# print("\n================= EDA REPORT =================")
# print("Executive summary: Bills and tips rise together; dinners and weekends")
# print("  drive the highest spend.")
# print("Findings:")
# print("  - total_bill is right-skewed.")
# print("  - total_bill & tip correlation ~",
#       round(tips['total_bill'].corr(tips['tip']), 2))
# print("  - Dinner/weekend bills are largest; Saturday is busiest.")
# print("Recommendations: upsell, push premium dinner/weekend menus, grow party size.")
