"""
============================================================================
EDA Case Study 1 — Student Performance Dataset
============================================================================
Goal : Perform a complete Exploratory Data Analysis (EDA) on a small student
       dataset to understand subject performance, spread, and class-level
       differences, then draw findings and recommendations.

EDA workflow used here:
    1. Inspect the data (shape, head)
    2. Descriptive statistics (describe)
    3. Patterns (group-based + subject analysis)
    4. Findings, insights and recommendations

Run:
    python case_study_1_student_performance.py
============================================================================
"""

import pandas as pd


# --------------------------------------------------------------------------
# 18.1  THE DATASET AND INSPECTION
# --------------------------------------------------------------------------
# Build the dataset in-memory. Each row is one student with their marks in
# three subjects. In a real project this would be loaded from a CSV/database.
students = pd.DataFrame({
    "Name":    ["Asha", "Ravi", "Imran", "Divya", "Karan", "Meena", "Sahil", "Tara"],
    "Class":   ["A", "A", "B", "B", "A", "B", "A", "B"],
    "Math":    [85, 60, 92, 45, 78, 55, 88, 40],
    "Science": [90, 65, 88, 50, 80, 60, 85, 48],
    "English": [82, 70, 95, 55, 76, 68, 90, 52],
})

# shape -> (rows, columns). Confirms we loaded 8 students and 5 columns.
print("Shape (rows, columns):", students.shape)

# head() -> first 5 rows. A quick visual sanity check of the data.
print("\nFirst rows (head):")
print(students.head())


# --------------------------------------------------------------------------
# 18.2  DESCRIPTIVE STATISTICS
# --------------------------------------------------------------------------
# Create a 'Total' column = sum of the three subject scores for each student.
# This single number summarises overall performance and is easy to compare.
students["Total"] = students["Math"] + students["Science"] + students["English"]

# describe() returns count, mean, std, min, quartiles and max for each column.
# .round(1) keeps the output readable. We look only at the numeric score columns.
print("\nDescriptive statistics:")
print(students[["Math", "Science", "English", "Total"]].describe().round(1))


# --------------------------------------------------------------------------
# 18.3  PATTERNS (GROUP-BASED AND SUBJECT ANALYSIS)
# --------------------------------------------------------------------------
# groupby("Class") splits students into Class A and Class B, then we take the
# mean Total of each group -> tells us which class performs better overall.
print("\nAverage Total by Class:")
print(students.groupby("Class")["Total"].mean().round(1))

# Subject averages across ALL students -> shows which subject is strongest
# and which is weakest on average.
print("\nSubject averages (all students):")
print(students[["Math", "Science", "English"]].mean().round(1))


# --------------------------------------------------------------------------
# 18.4  FINDINGS AND CONCLUSIONS
# --------------------------------------------------------------------------
# We print the interpretation so the script is self-explanatory when run.
print("""
------------------------- FINDINGS & CONCLUSIONS -------------------------
Finding 1 (subject): Math has the lowest average (67.9); English the highest (73.5).
    Insight: Students struggle most in Math.

Finding 2 (spread):  Totals range widely (140 to 275).
    Insight: There is a large performance gap between the strongest and
    weakest students.

Finding 3 (class):   Class A (237.2) clearly outperforms Class B (187.0).
    Insight: There is a notable ~50-point gap, so Class B as a whole needs
    more support.

Recommendation: Introduce additional Math support, focus on Class B, and give
    targeted help to the lowest-scoring students (Tara, Divya) to close the
    performance gap.
--------------------------------------------------------------------------
""")
