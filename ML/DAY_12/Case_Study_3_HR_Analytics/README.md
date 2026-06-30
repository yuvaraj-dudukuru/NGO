# Feature Engineering Case Study 3 — HR Analytics

**Goal:** Generate workforce metrics from raw employee data.

## Overview

A plain employee list becomes actionable workforce analytics by engineering
tenure, seniority, performance bands, and a **pay-equity** feature that compares
each salary to its department average.

| Feature | How it's built | What it tells you |
|---|---|---|
| `Experience` | `(today - JoinDate) / 365.25` years | Tenure |
| `SeniorityLevel` | `pd.cut` on `Experience` (Junior/Mid/Senior) | Career stage |
| `PerformanceLevel` | `pd.cut` on `PerformanceScore` (Low/Medium/High) | Performance band |
| `HighPerformer` | flag where `PerformanceScore >= 85` | Top-talent flag |
| `DeptAvgSalary` | `groupby(Department).transform("mean")` | Department benchmark |
| `VsDeptAvg%` | `Salary / DeptAvgSalary - 1` (%) | Pay vs. peers |

Reference date used for experience: **2026-06-18**.

## How to run

```bash
python hr_analytics_feature_engineering.py
```

Requires `pandas` and `numpy`:

```bash
pip install pandas numpy
```

## Expected output

```
    Name Department  Experience SeniorityLevel PerformanceLevel HighPerformer  VsDeptAvg%
0   Asha         IT         8.3         Senior             High           Yes        -5.3
1   Ravi         HR         2.8         Junior           Medium            No         0.0
2  Imran         IT        11.0         Senior             High           Yes        26.3
3  Divya    Finance         2.4         Junior              Low            No         0.0
4  Karan         IT         5.6            Mid           Medium            No       -21.1
```

> The IT department average salary is `(90000 + 120000 + 75000) / 3 = 95000`, so
> the `VsDeptAvg%` figures above are computed against that benchmark.

## Insight

Imran is a senior high performer paid **26.3% above** his department average
(well-rewarded), while Karan is paid **21.1% below** the IT average despite
mid-level experience (a potential pay-equity issue and attrition risk). These
engineered features turn a plain employee list into actionable workforce
analytics.

> Note: All names and values in this case study are fictional sample data used
> for demonstration only.
