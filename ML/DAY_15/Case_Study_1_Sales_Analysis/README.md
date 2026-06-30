# Business Analytics Case Study 1 — Sales Analysis

## Business context
A retail manager requires a statistical analysis of monthly sales to understand
performance, consistency, and any anomalies.

## Objective
Summarize monthly sales statistically and interpret the results.

## Data
Monthly sales (in thousands), January through October:

| Month | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Oct |
|-------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Sales | 210 | 225 | 240 | 250 | 265 | 280 | 290 | 310 | 330 | 980 |

## How to run
```bash
pip install pandas
python sales_analysis.py
```

## Code walkthrough
- `sales` — a `Series` of monthly sales, indexed by month.
- The `print` statements compute the **mean**, **median**, **standard deviation**, and **range**.
- The final block computes the IQR-based upper bound and identifies any month exceeding it.

The IQR (Interquartile Range) rule flags any value above
`Q3 + 1.5 × IQR` as a potential outlier.

## Output
```
Mean sales:    338.0
Median sales:  272.5
Std deviation: 228.6
Range:         770
Outlier(s): {'Oct': 980}
```

## Business interpretation
- The **mean** (338 thousand) is considerably higher than the **median**
  (272.5 thousand), and the large **standard deviation** (228.6 thousand)
  signals high variability.
- The IQR analysis identifies **October (980 thousand)** as an outlier — an
  exceptional month far above the others.

### Findings
- Typical monthly sales are around **272 thousand** (the median, not the
  inflated mean).
- Performance is otherwise fairly steady.
- October was anomalous and warrants investigation (a festival, a large order,
  or a data error).

### Recommendation
Base planning on the **median** and investigate the October spike to determine
whether it is repeatable or erroneous.
