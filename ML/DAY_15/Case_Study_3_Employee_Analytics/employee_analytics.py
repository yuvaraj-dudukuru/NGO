"""
Business Analytics Case Study 3 - Employee Analytics
====================================================

Business context:
    A Human Resources analyst must examine the relationships among employee
    experience, salary, and performance.

Objective:
    Compute descriptive statistics and the correlations among employee variables.
"""

import pandas as pd

emp = pd.DataFrame(
    {
        "Experience": [2, 4, 6, 8, 10, 12, 15, 20],
        "Salary": [35000, 45000, 55000, 68000, 80000, 95000, 110000, 140000],
        "Performance": [70, 74, 78, 82, 85, 88, 90, 95],
    }
)

# Full descriptive summary for every numeric column.
print("Descriptive statistics:")
print(emp.describe().round(1))

# Correlation matrix among the three variables.
print("\nCorrelation matrix:")
print(emp.corr().round(2))
