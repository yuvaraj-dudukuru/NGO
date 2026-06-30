"""
Business Analytics Case Study 3 - Employee Performance
=======================================================
Combines multi-table joins with KPI calculations and summary reporting.

Business context:
    HR data is spread across three tables: who the employees are, which
    department each belongs to (by code), and how each performed. To report by
    *department name* we must chain two joins, then aggregate.

Concepts demonstrated:
    * chained pd.merge(...)    - join 3 tables step by step (employees->dept->perf)
    * groupby().agg(...)       - several metrics per department in one pass
    * sort_values(...)         - rank departments by total sales

Run:
    python employee_performance.py
"""

import pandas as pd


def build_tables():
    """Return the three raw HR tables (employees, departments, performance)."""
    # Core employee record. DeptID is a *code* (D1/D2/D3), not a readable name.
    employees = pd.DataFrame({
        "EmpID": [1, 2, 3, 4, 5],
        "Name": ["Asha", "Ravi", "Imran", "Divya", "Karan"],  # synthetic names
        "DeptID": ["D1", "D2", "D1", "D3", "D1"],
    })
    # Lookup table that maps each department code to its human-readable name.
    departments = pd.DataFrame({
        "DeptID": ["D1", "D2", "D3"],
        "Department": ["IT", "HR", "Finance"],
    })
    # Performance metrics, keyed by EmpID.
    performance = pd.DataFrame({
        "EmpID": [1, 2, 3, 4, 5],
        "Sales": [120000, 80000, 95000, 150000, 110000],
        "Rating": [4.5, 3.8, 4.2, 4.9, 4.1],
    })
    return employees, departments, performance


def join_all(employees, departments, performance):
    """Join the three tables into one wide table.

    Step 1: attach the readable Department name using the DeptID code.
    Step 2: attach each employee's Sales and Rating using EmpID.
    Left joins keep every employee even if a lookup row were missing.
    """
    step1 = pd.merge(employees, departments, on="DeptID", how="left")
    full = pd.merge(step1, performance, on="EmpID", how="left")
    return full


def department_report(full):
    """Per-department KPI report, ranked by total sales.

    Produces four metrics per department in a single groupby pass: total and
    average sales, average rating, and head-count.
    """
    return full.groupby("Department").agg(
        Total_Sales=("Sales", "sum"),
        Avg_Sales=("Sales", "mean"),
        Avg_Rating=("Rating", "mean"),
        Employees=("Name", "count"),
    ).reset_index().sort_values("Total_Sales", ascending=False)


def main():
    employees, departments, performance = build_tables()
    full = join_all(employees, departments, performance)

    print("Joined table:")
    print(full[["Name", "Department", "Sales", "Rating"]])

    print("\nDepartment KPI report:")
    print(department_report(full))

    # Expected insight:
    #   IT has the most people and the highest total sales, but a single Finance
    #   employee (Divya) posts the top individual sales and rating - so "biggest
    #   team" and "best performer" are not the same story.


if __name__ == "__main__":
    main()
