# Day 15 — Statistics for Data Analysis

Hands-on statistics for data analysis with `pandas`: descriptive statistics,
distribution shape, correlation, and outlier detection — applied to realistic
business scenarios and translated into actionable recommendations.

All datasets in this folder are **synthetic** (no personal or real customer data).
Every output shown in the documentation was produced by **running the code**, not
copied from notes — a few figures here intentionally differ from the printed
course material, which contained arithmetic errors (see notes in the relevant
READMEs).

## Contents

### Case studies
Short, focused scenarios — each is a runnable script with its own README
(business context, code walkthrough, verified output, interpretation).

| # | Folder | Topic | Key technique |
|---|--------|-------|---------------|
| 1 | [Case_Study_1_Sales_Analysis](Case_Study_1_Sales_Analysis/) | Sales analysis | Mean / median / std, range, IQR outlier detection |
| 2 | [Case_Study_2_Customer_Analytics](Case_Study_2_Customer_Analytics/) | Customer analytics | `groupby` segment comparison of central tendency & dispersion |
| 3 | [Case_Study_3_Employee_Analytics](Case_Study_3_Employee_Analytics/) | Employee analytics | `describe()` + correlation matrix |

### Hands-on activity
| Folder | Topic | Format |
|--------|-------|--------|
| [Hands_On_Activity](Hands_On_Activity/) | Full statistical toolkit on one customer dataset | Jupyter notebook (`Day15_Statistics.ipynb`, saved with executed outputs) |

Applies mean, median, mode, variance, standard deviation, correlation, and IQR
outlier detection to a single dataset, step by step.

### Mini project
| Folder | Topic | Format |
|--------|-------|--------|
| [Mini_Project_MetroMart](Mini_Project_MetroMart/) | End-to-end customer analysis for a retailer (MetroMart) | Python script + written report |

A complete analysis of a 16-customer dataset: central tendency, dispersion,
distribution shape, percentiles, correlation, dual-method outlier detection
(IQR + z-score), and a business report with recommendations. See its
[REPORT.md](Mini_Project_MetroMart/REPORT.md).

## Folder structure
```
DAY_15/
├── README.md                          <- you are here
├── Case_Study_1_Sales_Analysis/
│   ├── sales_analysis.py
│   └── README.md
├── Case_Study_2_Customer_Analytics/
│   ├── customer_analytics.py
│   └── README.md
├── Case_Study_3_Employee_Analytics/
│   ├── employee_analytics.py
│   └── README.md
├── Hands_On_Activity/
│   ├── Day15_Statistics.ipynb
│   └── README.md
└── Mini_Project_MetroMart/
    ├── metromart_analysis.py
    ├── REPORT.md
    └── README.md
```

## Requirements
- Python 3.8+
- `pandas`, `numpy` (and `jupyter` to open the notebook)

```bash
pip install pandas numpy jupyter
```

## Run everything
From inside the `DAY_15/` folder:

```bash
python Case_Study_1_Sales_Analysis/sales_analysis.py
python Case_Study_2_Customer_Analytics/customer_analytics.py
python Case_Study_3_Employee_Analytics/employee_analytics.py
python Mini_Project_MetroMart/metromart_analysis.py
jupyter notebook Hands_On_Activity/Day15_Statistics.ipynb
```

## Concepts covered
- **Central tendency** — mean, median, mode, and when the mean misleads.
- **Dispersion** — range, variance, standard deviation, IQR.
- **Distribution shape** — detecting skew from the mean-vs-median gap.
- **Percentiles** — identifying top-tier customers (e.g. the top 10%).
- **Correlation** — correlation matrices and the correlation-vs-causation caveat.
- **Outlier detection** — the IQR rule and the z-score method.
- **Communication** — turning statistics into business findings and recommendations.
