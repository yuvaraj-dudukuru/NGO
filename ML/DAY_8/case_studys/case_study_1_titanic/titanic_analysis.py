# ============================================================================
# CASE STUDY 1 — TITANIC DATASET
# ----------------------------------------------------------------------------
# Goal: Perform a complete Exploratory Data Analysis (EDA) on the famous
#       Titanic passenger dataset using statistical visualizations.
#
# What you will practise here:
#   * Loading a built-in dataset with seaborn
#   * Checking for missing values BEFORE plotting (good Day-5 habit)
#   * Distribution plots, box plots, count plots and correlation heatmaps
#   * Reading a real human story out of the numbers
#
# How to run this file:
#   1. Install the libraries once:  pip install seaborn matplotlib pandas
#   2. From a terminal run:         python titanic_analysis.py
#   3. Each chart opens in its own window. Close a window to see the next one.
# ============================================================================

# --- Imports ----------------------------------------------------------------
# seaborn  -> high-level statistical plotting (built on top of matplotlib)
# matplotlib.pyplot -> lower-level plotting; we use it for titles and showing
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================================
# 21.1  LOADING AND INSPECTING THE DATA
# ============================================================================
# seaborn ships with a few example datasets. "titanic" is one of them, so we
# do not need to download a CSV file ourselves.
titanic = sns.load_dataset("titanic")

# Always LOOK at the data before plotting it.
# .head() shows the first 5 rows for the columns we care about most.
print("First 5 rows of key columns:")
print(titanic[["survived", "pclass", "sex", "age", "fare"]].head())

# Counting missing values is a cleaning habit from Day 5.
# .isnull() turns every cell into True/False (True = missing),
# and .sum() counts the True values per column.
# The Titanic data has REAL missing ages, which reminds us that
# cleaning must come before visualization.
print("\nMissing values per column:")
print(titanic.isnull().sum())


# ============================================================================
# 21.2  DISTRIBUTION PLOT — PASSENGER AGE
# ============================================================================
# A histogram shows HOW the values of a single numeric column are spread out.
#   x="age"   -> the column we are studying
#   bins=20   -> split the age range into 20 equal-width bars
#   kde=True  -> also draw a smooth curve (Kernel Density Estimate) over the bars
sns.histplot(data=titanic, x="age", bins=20, kde=True)
plt.title("Age Distribution of Passengers")
plt.show()  # display the figure, then wait for you to close it

# INTERPRETATION:
# Most passengers were young adults (roughly 20-40 years old). The shape is
# slightly RIGHT-SKEWED (a longer tail toward older ages) because there were
# fewer elderly passengers.


# ============================================================================
# 21.3  BOX PLOT — FARE BY PASSENGER CLASS
# ============================================================================
# A box plot summarizes a distribution with five numbers (min, Q1, median,
# Q3, max) and marks outliers as individual points.
#   x="pclass" -> grouping category (1st, 2nd, 3rd class)
#   y="fare"   -> the numeric value we compare across groups
sns.boxplot(data=titanic, x="pclass", y="fare")
plt.title("Fare by Passenger Class")
plt.show()

# INTERPRETATION:
# First-class fares are much higher and show many high OUTLIERS (very wealthy
# passengers). Third-class fares are low and tightly clustered together.
# The box plot reveals both the class difference AND the outlier passengers.


# ============================================================================
# 21.4  COUNT PLOT — SURVIVAL BY SEX
# ============================================================================
# A count plot is a bar chart that counts how many rows fall in each category.
#   x="sex"        -> one bar group per sex
#   hue="survived" -> split each group by survival (0 = died, 1 = survived)
sns.countplot(data=titanic, x="sex", hue="survived")
plt.title("Survival Count by Sex")
plt.show()

# INTERPRETATION:
# A far higher proportion of women survived than men — the famous
# "women and children first" rule. A count plot with a hue reveals this
# pattern instantly.


# ============================================================================
# 21.5  CORRELATION HEATMAP
# ============================================================================
# Correlation measures how strongly two numeric columns move together,
# from -1 (perfect opposite) through 0 (no link) to +1 (perfect together).
#   numeric_only=True -> ignore text columns (correlation needs numbers)
corr = titanic.corr(numeric_only=True)

# A heatmap draws the correlation table as a colored grid.
#   annot=True     -> print the number inside each cell
#   cmap="coolwarm"-> color scale (blue = negative, red = positive)
#   fmt=".2f"      -> show 2 decimal places
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Titanic Correlation Heatmap")
plt.show()

# INTERPRETATION:
# 'fare' has a POSITIVE correlation with 'survived' (wealthier passengers were
# more likely to survive). 'pclass' correlates NEGATIVELY with survival
# (a lower class NUMBER means a higher social class = better survival).
# The heatmap surfaces all of these relationships at a glance.


# ============================================================================
# 21.6  FINDINGS AND RECOMMENDATIONS
# ============================================================================
# * Finding : Survival was strongly linked to sex (women survived more) and to
#             class/fare (wealthier passengers survived more).
# * Insight : Social factors (gender norms and wealth/class) heavily influenced
#             who lived.
# * Caution : Correlation is NOT causation. Class correlates with survival, but
#             the real cause was LIFEBOAT ACCESS tied to class, not the class
#             label itself.
print("\nAnalysis complete. See the README for the full write-up.")
