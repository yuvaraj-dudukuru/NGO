"""
============================================================================
EDA Case Study 3 — Employee Dataset
============================================================================
Goal : Explore an employee dataset to understand the relationship between
       experience and salary, compare pay across departments, and check for
       salary outliers.

EDA workflow used here:
    1. Inspect the data (describe)
    2. Relationship analysis (correlation) + group analysis (dept salaries)
    3. Outlier check on Salary
    4. Findings, insights and recommendations

Run:
    python case_study_3_employee.py
============================================================================
"""

import pandas as pd


# --------------------------------------------------------------------------
# 20.1  THE DATASET AND INSPECTION
# --------------------------------------------------------------------------
# Each row is one employee: their department, age, salary and years of
# experience.
emp = pd.DataFrame({
    "Name":       ["Asha", "Ravi", "Imran", "Divya", "Karan", "Meena", "Sahil", "Tara"],
    "Department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "Age":        [25, 32, 28, 45, 23, 38, 29, 41],
    "Salary":     [40000, 55000, 50000, 90000, 35000, 60000, 75000, 52000],
    "Experience": [2, 8, 4, 20, 1, 12, 9, 15],
})

# describe() gives count/mean/std/min/quartiles/max for every numeric column.
# A fast way to understand the scale and spread of Age, Salary, Experience.
print("Descriptive statistics:")
print(emp.describe().round(1))


# --------------------------------------------------------------------------
# 20.2  RELATIONSHIP AND GROUP ANALYSIS
# --------------------------------------------------------------------------
# .corr() measures the linear relationship between Experience and Salary.
# Result ranges from -1 to +1; close to +1 means "more experience tends to
# come with higher salary".
corr = emp["Experience"].corr(emp["Salary"])
print("\nCorrelation (Experience vs Salary):", round(corr, 2))

# groupby("Department") + mean Salary -> average pay in each department,
# revealing which departments pay the most on average.
print("\nAverage salary by department:")
print(emp.groupby("Department")["Salary"].mean().round(0))


# --------------------------------------------------------------------------
# 20.3  OUTLIER CHECK
# --------------------------------------------------------------------------
# Comparing the maximum salary against the median is a quick outlier check:
# a max far above the median suggests one unusually high earner.
print("\nMax salary:", emp["Salary"].max(),
      "| Median salary:", emp["Salary"].median())


# --------------------------------------------------------------------------
# 20.4  FINDINGS AND CONCLUSIONS
# --------------------------------------------------------------------------
print("""
------------------------- FINDINGS & CONCLUSIONS -------------------------
Finding 1: Experience and Salary are strongly correlated (0.81).
    Insight: Salary rises clearly with years of experience.

Finding 2: Finance pays the most on average (82,500), then HR (57,500),
    then IT (44,250).
    Insight: Department strongly influences pay level.

Finding 3: The maximum salary (90,000) sits well above the median (53,500).
    Insight: The highest earner (Divya, 20 yrs experience, Finance) is a
    high-end outlier consistent with seniority - not an error.

Recommendation: Use the experience-salary link for fair, transparent pay
    bands; review IT salaries if retention is a concern, and ensure senior
    Finance pay reflects genuine experience.
--------------------------------------------------------------------------
""")
