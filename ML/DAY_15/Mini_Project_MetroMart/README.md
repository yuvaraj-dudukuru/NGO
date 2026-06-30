# Mini Project — MetroMart Customer Statistical Analysis

## Problem statement
You are a data analyst at **MetroMart**, a retail company. Given a dataset of
customer transactions, conduct a complete statistical analysis to characterize
customer behaviour, identify relationships, detect anomalies, and produce
business recommendations.

## Files
| File | Purpose |
|------|---------|
| [metromart_analysis.py](metromart_analysis.py) | Full analysis script (runnable). |
| [REPORT.md](REPORT.md) | The written business report with verified findings & recommendations. |
| README.md | This file. |

## The dataset
A **synthetic** dataset of 16 customers (no real customer data). It is
deliberately built so that:
- **Spending is right-skewed** and contains a clear high-value outlier (**C16**);
- **Visits and spending are positively related**;
- One spending value (20,000) repeats, so the **mode** is meaningful.

Variables: `Customer`, `Age`, `Spending` (annual), `Visits`, `BasketValue`
(average basket value).

| Customer | Age | Spending | Visits | BasketValue |
|----------|-----|----------|--------|-------------|
| C1  | 25 | 12000  | 5  | 1500 |
| C2  | 32 | 25000  | 12 | 2000 |
| C3  | 28 | 8000   | 3  | 1200 |
| C4  | 45 | 30000  | 15 | 2200 |
| C5  | 31 | 18000  | 8  | 1800 |
| C6  | 52 | 10000  | 4  | 1300 |
| C7  | 29 | 22000  | 11 | 2100 |
| C8  | 38 | 15000  | 7  | 1600 |
| C9  | 41 | 28000  | 13 | 2150 |
| C10 | 36 | 20000  | 9  | 1900 |
| C11 | 48 | 13000  | 6  | 1400 |
| C12 | 27 | 29000  | 14 | 2300 |
| C13 | 33 | 20000  | 10 | 2000 |
| C14 | 55 | 6000   | 2  | 1100 |
| C15 | 30 | 33000  | 16 | 2500 |
| C16 | 44 | 150000 | 20 | 4000 |

## How to run
```bash
pip install pandas numpy
python metromart_analysis.py
```

## Required analysis (and where it lives)
The script prints seven labelled sections:

1. **Central tendency** — mean, median, mode of spending; skew check.
2. **Dispersion** — range, standard deviation, IQR.
3. **Distribution shape** — classified via the mean-vs-median gap.
4. **Percentiles** — the 90th-percentile (top-10%) spending threshold.
5. **Correlation** — correlation matrix among Age, Spending, Visits, BasketValue;
   strongest relationship + correlation-vs-causation caveat.
6. **Outlier detection** — both the IQR rule and the z-score method.
7. **Insights & recommendations** — typical profile, most valuable customer,
   and three+ recommendations.

## Verified key results
| Measure | Value |
|---------|-------|
| Mean spending | 27,437.5 |
| Median spending | 20,000 |
| Mode spending | 20,000 |
| Range | 144,000 (6,000 → 150,000) |
| Standard deviation | 33,704.5 |
| IQR (Q1 12,750 → Q3 28,250) | 15,500 |
| Distribution shape | Right-skewed (mean is +37% above median) |
| Top-10% threshold (P90) | 31,500 → customers **C16, C15** |
| Strongest correlation | Visits ↔ BasketValue (r = 0.93) |
| Visits ↔ Spending | r = 0.73 (moderate-to-strong) |
| IQR outlier | C16 (150,000) |
| Z-score outlier (\|z\| > 3) | C16 (z = 3.76) |

> All figures above are computed by the script and were verified by running it.
> See [REPORT.md](REPORT.md) for the full narrative and recommendations.
