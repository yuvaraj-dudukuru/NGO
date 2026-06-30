"""
Feature Engineering Case Study 3 — HR Analytics
===============================================
Goal: Generate workforce metrics from raw employee data.

The raw table only stores a join date, a salary, and a performance score. HR
decisions need richer, comparable features: how long someone has worked here,
their seniority band, whether they are a high performer, and how their pay
compares to their own department's average. We engineer all of those below.

Run:
    python hr_analytics_feature_engineering.py
"""

import pandas as pd
import numpy as np


def build_raw_data():
    """Return the raw employee table (the columns we start from)."""
    return pd.DataFrame({
        "Name": ["Asha", "Ravi", "Imran", "Divya", "Karan"],   # synthetic names
        "Department": ["IT", "HR", "IT", "Finance", "IT"],
        "JoinDate": pd.to_datetime([
            "2018-03-01", "2023-08-15", "2015-06-10",
            "2024-01-20", "2020-11-05",
        ]),
        "Salary": [90000, 55000, 120000, 60000, 75000],
        "PerformanceScore": [88, 72, 95, 65, 80],
    })


def engineer_features(emp, today):
    """Add tenure, seniority, performance, and pay-equity features.

    `today` is the reference date tenure is measured against (passed in for
    reproducible results).
    """
    # Tenure in years: days since joining / 365.25 (the .25 accounts for leap years).
    emp["Experience"] = ((today - emp["JoinDate"]).dt.days / 365.25).round(1)

    # Seniority band from tenure: pd.cut buckets continuous years into 3 labels.
    emp["SeniorityLevel"] = pd.cut(
        emp["Experience"],
        bins=[0, 3, 7, 100],                       # <=3 Junior, <=7 Mid, else Senior
        labels=["Junior", "Mid", "Senior"],
    )

    # Performance band from the raw score, for easy reading in a report.
    emp["PerformanceLevel"] = pd.cut(
        emp["PerformanceScore"],
        bins=[0, 70, 85, 100],                     # <=70 Low, <=85 Medium, else High
        labels=["Low", "Medium", "High"],
    )

    # Simple Yes/No high-performer flag (>= 85). np.where is a vectorised if/else.
    emp["HighPerformer"] = np.where(emp["PerformanceScore"] >= 85, "Yes", "No")

    # Pay-equity feature: compare each salary to its OWN department's average.
    # groupby(...).transform("mean") returns a value for EVERY row (the dept mean),
    # so it aligns back onto the original rows - unlike .mean() which would collapse
    # the table. This lets us compute a per-person "above/below dept average" figure.
    emp["DeptAvgSalary"] = (
        emp.groupby("Department")["Salary"].transform("mean").round(0)
    )
    emp["VsDeptAvg%"] = ((emp["Salary"] / emp["DeptAvgSalary"] - 1) * 100).round(1)
    return emp


def main():
    emp = build_raw_data()
    today = pd.Timestamp("2026-06-18")   # fixed "as of" date for reproducibility

    emp = engineer_features(emp, today)

    print("=" * 70)
    print("Workforce analytics table")
    print("=" * 70)
    print(emp[[
        "Name", "Department", "Experience", "SeniorityLevel",
        "PerformanceLevel", "HighPerformer", "VsDeptAvg%",
    ]])

    # Expected insight:
    #   Imran (Senior IT) is the most experienced, top performer, and paid well
    #   above the IT average; Ravi (HR) sits below his only-department baseline.
    #   VsDeptAvg% surfaces pay gaps fairly, comparing like-with-like.


if __name__ == "__main__":
    main()
