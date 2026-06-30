# Business Analytics Case Study 3 — Employee Performance

A hands-on case study combining **multi-table joins** (three tables) with **KPI
calculations** and a ranked **summary report** — the standard structure of real HR
analytics.

## Files

| File | Description |
|------|-------------|
| `employee_performance.py` | Runnable script: builds 3 tables, joins them, builds the KPI report |
| `README.md` | This document |

## Requirements

- Python 3.8+
- pandas

```bash
pip install pandas
```

## How to Run

```bash
python employee_performance.py
```

## The Tables

**employees**

| EmpID | Name  | DeptID |
|------:|-------|--------|
| 1 | Asha  | D1 |
| 2 | Ravi  | D2 |
| 3 | Imran | D1 |
| 4 | Divya | D3 |
| 5 | Karan | D1 |

**departments**

| DeptID | Department |
|--------|------------|
| D1 | IT |
| D2 | HR |
| D3 | Finance |

**performance**

| EmpID | Sales  | Rating |
|------:|-------:|-------:|
| 1 | 120000 | 4.5 |
| 2 |  80000 | 3.8 |
| 3 |  95000 | 4.2 |
| 4 | 150000 | 4.9 |
| 5 | 110000 | 4.1 |

## Analyses

### 1. Multi-Table Join (employees → departments → performance)

Two chained left joins assemble a single analysis-ready table:

```python
step1 = pd.merge(employees, departments, on="DeptID", how="left")
full  = pd.merge(step1, performance, on="EmpID", how="left")
print(full[["Name", "Department", "Sales", "Rating"]])
```

```
    Name Department   Sales  Rating
0   Asha         IT  120000     4.5
1   Ravi         HR   80000     3.8
2  Imran         IT   95000     4.2
3  Divya    Finance  150000     4.9
4  Karan         IT  110000     4.1
```

### 2. KPI Calculations and Summary Report

Named aggregations build a per-department KPI table, ranked by total sales:

```python
report = full.groupby("Department").agg(
    Total_Sales=("Sales", "sum"),
    Avg_Sales=("Sales", "mean"),
    Avg_Rating=("Rating", "mean"),
    Employees=("Name", "count"),
).reset_index().sort_values("Total_Sales", ascending=False)
print(report)
```

```
  Department  Total_Sales      Avg_Sales  Avg_Rating  Employees
2         IT       325000  108333.333333    4.266667          3
0    Finance       150000  150000.000000    4.900000          1
1         HR        80000   80000.000000    3.800000          1
```

> The left-most numbers (2, 0, 1) are the original row index preserved by
> `sort_values`. They are cosmetic only — the KPI values are unchanged. Add a final
> `.reset_index(drop=True)` if you prefer a clean 0, 1, 2 index.

## Insights and Recommendations

- **Finding:** IT has the highest total sales (₹325,000) and the most employees (3).
- **Finding:** Finance (Divya) has the highest average sales and rating, though just
  one employee.
- **Insight:** IT drives total volume; Finance has the single top performer
  (Divya: ₹150,000, 4.9 rating).
- **Recommendation:**
  - Recognize and retain Divya (the star performer).
  - Investigate whether IT's per-person sales can be raised.
  - Support HR, which lags in both sales and rating.

> This complete performance report required joining **three** tables — names live in
> `employees`, labels in `departments`, and metrics in `performance`. No single table
> could produce it alone.

## Key Concepts Demonstrated

- Chained `pd.merge(..., how="left")` across three related tables
- Resolving keys (`DeptID`, `EmpID`) that link the tables
- Multi-metric named aggregation (`sum`, `mean`, `count`) in one `.agg()`
- Ranking a summary report with `.sort_values(ascending=False)`
- Translating a joined KPI report into HR/performance recommendations
