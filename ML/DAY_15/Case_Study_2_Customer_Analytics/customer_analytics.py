"""
Business Analytics Case Study 2 - Customer Analytics
====================================================

Business context:
    A marketing team wishes to understand customer spending behaviour and
    compare two customer segments.

Objective:
    Compare the spending of Premium and Regular customer segments statistically.
"""

import pandas as pd

df = pd.DataFrame(
    {
        "Segment": [
            "Premium", "Premium", "Premium", "Premium",
            "Regular", "Regular", "Regular", "Regular",
        ],
        "Spending": [45000, 52000, 48000, 60000, 8000, 12000, 9000, 15000],
    }
)

# Group by segment and compute central tendency and dispersion.
summary = df.groupby("Segment")["Spending"].agg(["mean", "median", "std"])
print(summary.round(1))
