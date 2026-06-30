# Case Study 1 — Retail Sales Analysis

> Identify the yearly **trend**, the **peak period**, and the **seasonal effect**
> in twelve months of retail sales.

---

## 1. Business Context

A retail manager requires an analysis of monthly sales over a full year to:

- assess the overall **trend** (is the business growing or declining?),
- identify the **strongest sales periods**, and
- detect **seasonality** (recurring high/low periods).

## 2. Objective

> **Analyze monthly sales to identify the trend and the peak period.**

## 3. Dataset

Twelve rows, one per month of 2025.

| Field       | Type           | Description                                  |
|-------------|----------------|----------------------------------------------|
| `Month`     | datetime       | First day of each month (Jan–Dec 2025)       |
| `Sales`     | integer        | Sales for that month (₹, thousands implied)  |
| `MonthName` | string (derived)| Human-readable month label, e.g. `December` |

```
Sales: 200, 210, 220, 215, 230, 225, 240, 235, 260, 290, 350, 420
```

## 4. How to Run

```bash
# from this folder
pip install pandas
python retail_sales_analysis.py
```

## 5. Method — Line by Line

| Code | What it does |
|------|--------------|
| `pd.to_datetime([...])` | Parses the month strings into real datetime values so date methods are available. |
| `df["Month"].dt.month_name()` | Extracts a readable month name (`January`, `February`, …). |
| `df["Sales"].sum()` | Annual total sales. |
| `df["Sales"].mean()` | Average monthly sales (the reference level). |
| `df.loc[df["Sales"].idxmax(), "MonthName"]` | `idxmax` finds the index of the highest sales month; `.loc` returns its name. |
| `df.loc[df["Sales"].idxmin(), "MonthName"]` | Same idea for the lowest month. |
| `df["Sales"][:6].sum()` vs `df["Sales"][6:].sum()` | Compares the first half of the year to the second half to reveal the direction of the trend. |

## 6. Expected Output

```
Total annual sales: 3095
Average monthly sales: 257.9
Peak month: December
Lowest month: January
First half total: 1300 | Second half total: 1795
```

> **Note:** These are the values the script actually computes from the dataset
> above. (Some printed copies of this exercise quote `3140`, `261.7`, and `1840`;
> those contain arithmetic slips — the sum of the twelve sales figures is `3095`.)

## 7. Business Interpretation

- **Trend:** A clear **upward trend** runs through the year — the second half
  (**₹1,795**) substantially outperforms the first half (**₹1,300**).
- **Seasonality:** Sales **peak sharply in December (₹420)**, driven by festival
  and holiday shopping — a strong seasonal effect.
- **Findings:** The business is **growing**, and the **final quarter — especially
  December — is the critical sales period**.

### Recommendations

1. Ensure **ample inventory** and **marketing investment** ahead of the festival season.
2. Investigate the **November→December surge** to understand and maximize its capture.

## 8. Key Takeaway

This case study demonstrates the combined identification of **trend** (upward
through the year) and **seasonality** (the December peak) — the two effects that
sit at the heart of retail time-series analysis.
