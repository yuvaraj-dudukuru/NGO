# Day 15 — Hands-On Activity: Statistics on a Single Dataset

A guided Jupyter notebook ([Day15_Statistics.ipynb](Day15_Statistics.ipynb)) that
applies the full statistical toolkit — mean, median, mode, variance, standard
deviation, correlation, and outlier detection — to one customer dataset, then
translates the results into business findings.

## Dataset
| Customer | Age | Spending | Visits |
|----------|-----|----------|--------|
| C1  | 25 | 12000  | 5  |
| C2  | 32 | 25000  | 12 |
| C3  | 28 | 8000   | 3  |
| C4  | 45 | 30000  | 15 |
| C5  | 31 | 18000  | 8  |
| C6  | 52 | 10000  | 4  |
| C7  | 29 | 22000  | 11 |
| C8  | 38 | 15000  | 7  |
| C9  | 41 | 28000  | 13 |
| C10 | 27 | 150000 | 20 |

## How to run
```bash
pip install pandas numpy jupyter
jupyter notebook Day15_Statistics.ipynb
```
The notebook is saved with its outputs already executed, so it can also just be
read top to bottom.

## Steps in the notebook
1. **Load the dataset** — build the customer `DataFrame`.
2. **Mean** of spending.
3. **Median** of spending (compared against the mean to detect skew).
4. **Mode** of visits.
5. **Variance** of spending.
6. **Standard deviation** of spending.
7. **Correlation matrix** of Age, Spending, Visits.
8. **Interpret** the results.
9. **Detect outliers** with the IQR rule and record findings.

## Verified output
```
Mean spending: 31800.0
Median spending: 20000.0
Mode of Visits: [3, 4, 5, 7, 8, 11, 12, 13, 15, 20]
Variance of spending: 1781955555.6
Standard deviation of spending: 42213.2

           Age  Spending  Visits
Age       1.00     -0.27   -0.07
Spending -0.27      1.00    0.79
Visits   -0.07      0.79    1.00

Spending outliers:
  Customer  Spending
9      C10    150000
```

## Findings
- **Typical spending is 20,000** (the median), not the 31,800 mean, which is
  inflated by one outlier.
- **Customer C10 is an outlier**, spending 150,000 — a high-value customer
  warranting special attention.
- **Visits and spending are strongly correlated** (0.79), suggesting that
  increasing customer visits may be associated with increased spending.
- **Age shows no meaningful relationship** to spending or visits.

## Note on the numbers
The figures above are the **actual values computed by pandas** from the dataset.
They differ slightly from some figures circulating in the printed course material,
which contained arithmetic errors:

| Measure | Printed (incorrect) | Computed (this notebook) |
|---------|--------------------|---------------------------|
| Variance of spending | 1,738,400,000.0 | **1,781,955,555.6** |
| Std deviation of spending | 41,693.6 | **42,213.2** |
| Spending ↔ Visits correlation | 0.55 | **0.79** |
| Age ↔ Spending correlation | −0.05 | **−0.27** |

The overall conclusions (right skew, one outlier, visits↔spending link, age
largely unrelated) are unchanged.
