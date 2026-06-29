# ============================================================================
# CASE STUDY 3 — STUDENT PERFORMANCE
# ----------------------------------------------------------------------------
# Goal: Explore how study hours relate to exam marks, and how subjects relate
#       to one another, for a small group of students.
#
# What you will practise here:
#   * Building a DataFrame with both text and numeric columns
#   * Scatter plots with a category hue to check if a pattern holds per group
#   * Correlation heatmaps to compare several numeric columns at once
#   * Bar plots to compare a group average
#
# How to run this file:
#   1. Install the libraries once:  pip install pandas seaborn matplotlib
#   2. From a terminal run:         python student_performance.py
#   3. Each chart opens in its own window. Close a window to see the next one.
# ============================================================================

# --- Imports ----------------------------------------------------------------
# pandas  -> tables (DataFrames)
# seaborn -> statistical plotting
# matplotlib.pyplot -> titles and showing the figures
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# ============================================================================
# 23.1  THE DATA AND SETUP
# ============================================================================
# Each student has: a Name, a Class (A or B), the number of StudyHours per day,
# and Math and Science marks out of 100. Every list has 8 values (8 students).
students = pd.DataFrame({
    "Name":       ["Asha", "Ravi", "Imran", "Divya", "Karan", "Meena", "Sahil", "Tara"],
    "Class":      ["A", "A", "B", "B", "A", "B", "A", "B"],
    "StudyHours": [6, 3, 8, 2, 5, 3, 7, 4],
    "Math":       [85, 60, 92, 45, 78, 55, 88, 65],
    "Science":    [90, 65, 88, 50, 80, 60, 85, 68],
})


# ============================================================================
# 23.2  RELATIONSHIP — STUDY HOURS vs MATH MARKS
# ============================================================================
# Scatter plot of study time against Math marks. Coloring by Class lets us see
# whether the same trend appears in BOTH classes.
#   x="StudyHours" -> horizontal axis
#   y="Math"       -> vertical axis
#   hue="Class"    -> color dots by class (A vs B)
sns.scatterplot(data=students, x="StudyHours", y="Math", hue="Class")
plt.title("Study Hours vs Math Marks by Class")
plt.show()

# INTERPRETATION:
# A clear POSITIVE relationship — more study hours generally means higher marks.
# The hue lets us confirm the pattern holds across both classes.


# ============================================================================
# 23.3  CORRELATION HEATMAP
# ============================================================================
# Compute correlations among all numeric columns (StudyHours, Math, Science).
#   numeric_only=True -> skip the text columns (Name, Class)
corr = students.corr(numeric_only=True)

# Draw the correlation table as a colored grid.
#   annot=True   -> write the number in each cell
#   cmap="YlGnBu"-> yellow-green-blue color scale
#   fmt=".2f"    -> 2 decimal places
sns.heatmap(corr, annot=True, cmap="YlGnBu", fmt=".2f")
plt.title("Student Performance Correlation")
plt.show()

# INTERPRETATION:
# Study hours correlate strongly with BOTH Math and Science. Math and Science
# also correlate strongly with each other (good students tend to do well in
# both subjects).


# ============================================================================
# 23.4  CATEGORY COMPARISON — AVERAGE MATH BY CLASS
# ============================================================================
# Bar plot comparing the average Math mark of Class A vs Class B.
#   x="Class" -> one bar per class
#   y="Math"  -> bar height = average Math mark
sns.barplot(data=students, x="Class", y="Math")
plt.title("Average Math Marks by Class")
plt.show()

# INTERPRETATION:
# Reveals which class performs better on average in Math.


# ============================================================================
# 23.5  FINDINGS
# ============================================================================
# * Study hours strongly drive marks — the clearest, most actionable
#   relationship in the data.
# * Performance in Math and Science moves together.
# * Recommendation: Encourage more study time. Students strong in one science
#   subject tend to be strong in the other, so support struggling students
#   broadly rather than subject-by-subject.
print("\nAnalysis complete. See the README for the full write-up.")
