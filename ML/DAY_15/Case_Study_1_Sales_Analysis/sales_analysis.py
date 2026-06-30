"""
Business Analytics Case Study 1 - Sales Analysis
================================================

Business context:
    A retail manager requires a statistical analysis of monthly sales to
    understand performance, consistency, and any anomalies.

Objective:
    Summarize monthly sales statistically and interpret the results.
"""

import pandas as pd

# Monthly sales (in thousands), indexed by month.
sales = pd.Series(
    [210, 225, 240, 250, 265, 280, 290, 310, 330, 980],
    index=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"],
)

# Central tendency and dispersion.
print("Mean sales:   ", round(sales.mean(), 1))
print("Median sales: ", sales.median())
print("Std deviation:", round(sales.std(), 1))
print("Range:        ", sales.max() - sales.min())

# Outlier check using the IQR rule.
q1, q3 = sales.quantile(0.25), sales.quantile(0.75)
iqr = q3 - q1
upper = q3 + 1.5 * iqr
print("Outlier(s):", sales[sales > upper].to_dict())
