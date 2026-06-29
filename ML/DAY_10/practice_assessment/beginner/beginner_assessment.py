"""
================================================================================
BEGINNER PRACTICE ASSESSMENT
================================================================================
Dataset: 5 employees (Name, Department, Salary) — already CLEAN.

Tasks:
    1. Load into a DataFrame; print head() and describe().
    2. Find the average salary.
    3. Find the highest-paid employee.
    4. Count employees per department with value_counts().
    5. Create a bar chart of salary by employee.
================================================================================
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")              # save chart without a display
import matplotlib.pyplot as plt
import seaborn as sns

# --- Task 1: Load & inspect --------------------------------------------------
df = pd.DataFrame({
    "Name":       ["Asha", "Ravi", "Imran", "Sneha", "Karan"],
    "Department": ["Sales", "Engineering", "Sales", "HR", "Engineering"],
    "Salary":     [55000, 90000, 48000, 60000, 95000],
})
print("head():")
print(df.head())
print("\ndescribe():")           # count/mean/std/min/quartiles/max for Salary
print(df.describe())

# --- Task 2: Average salary --------------------------------------------------
# .mean() averages the numeric column.
avg = df["Salary"].mean()
print("\nAverage salary:", avg)         # 69600.0

# --- Task 3: Highest-paid employee -------------------------------------------
# Sort descending and take the top row.
top = df.sort_values("Salary", ascending=False).head(1)
print("\nHighest-paid employee:")
print(top)                              # Karan, Engineering, 95000

# --- Task 4: Employees per department ----------------------------------------
# value_counts() tallies each category.
print("\nEmployees per department:")
print(df["Department"].value_counts())  # Sales 2, Engineering 2, HR 1

# --- Task 5: Bar chart of salary by employee ---------------------------------
# A bar chart compares a value across distinct labels (here, people).
sns.set_theme(style="whitegrid")
plt.figure()
sns.barplot(data=df, x="Name", y="Salary")
plt.title("Salary by Employee"); plt.xlabel("Employee"); plt.ylabel("Salary")
plt.tight_layout()
plt.savefig("salary_by_employee.png", dpi=150)
print("\nSaved chart -> salary_by_employee.png")
