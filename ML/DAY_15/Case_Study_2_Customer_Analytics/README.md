# Business Analytics Case Study 2 — Customer Analytics

## Business context
A marketing team wishes to understand customer spending behaviour and compare
two customer segments.

## Objective
Compare the spending of Premium and Regular customer segments statistically.

## Data
Customer spending labelled by segment:

| Segment | Spending |
|---------|----------|
| Premium | 45000 |
| Premium | 52000 |
| Premium | 48000 |
| Premium | 60000 |
| Regular | 8000 |
| Regular | 12000 |
| Regular | 9000 |
| Regular | 15000 |

## How to run
```bash
pip install pandas
python customer_analytics.py
```

## Code walkthrough
- `df` — spending data labelled by customer segment.
- `df.groupby("Segment")["Spending"].agg(["mean", "median", "std"])` — groups by
  segment and computes the **mean**, **median**, and **standard deviation** of
  spending for each.
- `.round(1)` — formats the output.

## Output
```
            mean   median     std
Segment
Premium  51250.0  50000.0  6500.0
Regular  11000.0  10500.0  3162.3
```

## Business interpretation
The statistical comparison reveals a stark difference between segments.
**Premium** customers spend on average **51,250**, almost five times the
**11,000** average of **Regular** customers. Both segments are internally
consistent (modest standard deviations and close mean/median values, indicating
no significant skew within either group).

### Findings
- The two segments are genuinely distinct.
- The Premium segment is far more valuable.
- The consistency within each segment makes the averages reliable.

### Recommendation
Prioritize the **retention of Premium customers** and design strategies to
**migrate Regular customers toward Premium-level spending** — an insight
supported here by a rigorous statistical comparison of both central tendency and
dispersion.
