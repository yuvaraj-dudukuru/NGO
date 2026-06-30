# Case Study 3 — Employee Performance Analysis

**Business context.** A human resources team requires an analysis of employee
performance by department, including a performance classification and a
departmental summary suitable for a dashboard.

## Files

| File | Description |
|------|-------------|
| `employee_data.csv` | The raw dataset: `Employee, Department, Score` |
| `Employee_Performance.xlsx` | Workbook with the classification formula, a department summary, conditional formatting, and a chart |

> Employee names are generic placeholders (`Employee 1` … `Employee 7`).

## The dataset

| Employee | Department | Score |
|----------|-----------|------:|
| Employee 1 | IT | 92 |
| Employee 2 | IT | 88 |
| Employee 3 | IT | 81 |
| Employee 4 | Finance | 85 |
| Employee 5 | Finance | 79 |
| Employee 6 | HR | 78 |
| Employee 7 | HR | 70 |

## The analysis

**1. Performance classification** (sheet *Employee Data*). Each employee is
classified with a nested `IF`:

```
=IF(Score>=85, "High", IF(Score>=70, "Medium", "Low"))
```

**2. Department summary** (sheet *Department Summary*). A PivotTable with
**Department** in Rows and the **Average of Score** in Values produces the
departmental summary. The workbook reproduces this with `AVERAGEIF` and `COUNTIF`:

| Department | Avg Performance | Employees |
|-----------|----------------:|----------:|
| IT | 87 | 3 |
| Finance | 82 | 2 |
| HR | 74 | 2 |

**3. Conditional formatting.** The highest-performing department is highlighted in
**green** and the lowest in **red**, directing attention to the extremes. A
**PivotChart / bar chart** visualises the comparison.

## Business interpretation

The analysis classifies each employee's performance and summarises performance by
department, with conditional formatting emphasising the best and worst performers.

**Findings.** The **IT** department performs best (avg 87) and **HR** lags
(avg 74).

**Recommendations.** Document and replicate the practices of the high-performing
department; investigate and support the lower-performing one.

This case study demonstrates the integration of **logical functions, PivotTables,
conditional formatting, and PivotCharts** into a complete performance dashboard —
the kind of deliverable HR teams rely upon.

## Rebuild it yourself

1. **Data → From Text/CSV** → import `employee_data.csv`.
2. Add a `Performance Level` column with the nested `IF` above, copy down.
3. **Insert → PivotTable**: Department → Rows; Score → Values (set to *Average*).
4. **Home → Conditional Formatting** to highlight the top/bottom departments.
5. Add a **PivotChart** comparing average performance by department.
