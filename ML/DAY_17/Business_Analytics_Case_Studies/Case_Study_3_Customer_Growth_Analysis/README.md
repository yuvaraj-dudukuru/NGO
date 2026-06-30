# Case Study 3 — Customer Growth Analysis

> Measure both the **cumulative customer base** and the **month-over-month
> acquisition rate** for a subscription business.

---

## 1. Business Context

A subscription business wishes to analyze its customer growth over the year,
including the **rate of new customer acquisition**.

## 2. Objective

> **Analyze monthly new and cumulative customers to assess the growth trend.**

## 3. Dataset

Twelve rows, one per month.

| Field            | Type            | Description                                          |
|------------------|-----------------|------------------------------------------------------|
| `Month`          | string          | Month label (`Jan` … `Dec`)                          |
| `NewCustomers`   | integer         | New customers acquired that month                    |
| `TotalCustomers` | integer (derived)| Running total (cumulative sum) of customers          |
| `GrowthRate%`    | float (derived) | Month-over-month % change in new customers           |

```
NewCustomers: 100, 120, 130, 125, 150, 160, 175, 190, 210, 230, 260, 300
```

## 4. How to Run

```bash
# from this folder
pip install pandas
python customer_growth_analysis.py
```

## 5. Method — Line by Line

| Code | What it does |
|------|--------------|
| `df["NewCustomers"].cumsum()` | **Cumulative sum** — the running total of customers over time. |
| `df["NewCustomers"].pct_change() * 100` | **Percentage change** in new customers from one month to the next (month-over-month growth rate). |
| `.round(1)` | Rounds the growth rate to one decimal place for readability. |

> The first `GrowthRate%` value is `NaN` because there is no prior month to
> compare against.

## 6. Expected Output (abridged)

```
   Month  NewCustomers  TotalCustomers  GrowthRate%
0    Jan           100             100          NaN
1    Feb           120             220         20.0
2    Mar           130             350          8.3
...
11   Dec           300            2150         15.4

Total customers by December: 2150
```

> **Note:** The cumulative total is `2150` — the sum of the twelve monthly
> acquisition figures. (Some printed copies quote `2350`; that is an arithmetic
> slip.)

## 7. Business Interpretation

- **Growth:** Both **new acquisition** and the **total customer base** grow
  strongly all year; the cumulative total reaches **2,150 customers by December**.
- **Acceleration:** Month-over-month growth is **consistently positive**, and the
  **pace of acquisition accelerates in the second half** of the year.
- **Findings:** The business is in a **healthy growth phase with accelerating
  acquisition**.

### Recommendations

1. **Sustain the acquisition strategy** that is driving the latter-half acceleration.
2. Ensure the **operational capacity** to serve a rapidly growing customer base is in place.

## 8. Key Takeaway

The combination of the **cumulative sum** (size of the base) and the
**growth rate** (speed of change) illustrates two essential time-series
techniques for analyzing growth.
