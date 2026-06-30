# Business Analytics Case Study 1 — Retail Sales

A hands-on case study applying **GroupBy**, **aggregations**, and **pivot tables**
to a small, realistic retail dataset using pandas.

## Files

| File | Description |
|------|-------------|
| `retail_sales_analysis.py` | Runnable script with the dataset and all three analyses |
| `README.md` | This document |

## Requirements

- Python 3.8+
- pandas

```bash
pip install pandas
```

## How to Run

```bash
python retail_sales_analysis.py
```

## The Data

8 sales records across 3 regions and 3 product categories:

| Region | Category | Units | Revenue |
|--------|----------|------:|--------:|
| North  | Elec     |  5    | 50000   |
| South  | Groc     | 20    | 12000   |
| East   | Elec     |  8    | 60000   |
| North  | Cloth    | 15    |  9000   |
| South  | Elec     |  6    | 55000   |
| East   | Groc     | 25    | 14000   |
| North  | Elec     | 10    | 80000   |
| East   | Cloth    | 12    |  7000   |

## Analyses

### 1. GroupBy — Revenue by Region

```python
sales.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
```

```
Region
North    139000
East      81000
South     67000
Name: Revenue, dtype: int64
```

### 2. Multi-Aggregation — KPIs by Category

Named aggregations produce a clean KPI table in one pass:

```python
sales.groupby("Category").agg(
    Total_Revenue=("Revenue", "sum"),
    Avg_Revenue=("Revenue", "mean"),
    Total_Units=("Units", "sum"),
).reset_index()
```

```
  Category  Total_Revenue  Avg_Revenue  Total_Units
0    Cloth          16000       8000.0           27
1     Elec         245000      61250.0           29
2     Groc          26000      13000.0           45
```

### 3. Pivot Table — Region × Category Revenue

```python
pd.pivot_table(sales, index="Region", columns="Category",
               values="Revenue", aggfunc="sum", fill_value=0, margins=True)
```

```
Category  Cloth    Elec   Groc     All
Region
East       7000   60000  14000   81000
North      9000  130000      0  139000
South         0   55000  12000   67000
All       16000  245000  26000  287000
```

## Insights and Recommendations

- **Finding:** North is the top region (₹139,000), driven almost entirely by
  Electronics (₹130,000 of its ₹139,000).
- **Finding:** Electronics dominates revenue (₹245,000) despite Grocery selling the
  most units (45 units) — a classic *high-value vs. high-volume* pattern.
- **Insight:** Electronics is the leading category in **every** region; revenue is
  most concentrated in North (₹130,000), then East (₹60,000) and South (₹55,000).
- **Insight:** East is the most balanced region, earning across all three categories
  (Elec ₹60,000, Groc ₹14,000, Cloth ₹7,000).
- **Recommendation:**
  - Prioritize Electronics stock in North and East.
  - Use Grocery (high units) to drive footfall and upsell Electronics.
  - South relies heavily on a single Electronics line — diversify its category mix.

> **Note on the source figures:** The "Output" blocks in the original case-study
> brief contained values that do not match the dataset (e.g. East revenue, Electronics
> unit count, and the Grocery column of the pivot). The numbers above are the
> **verified output of `retail_sales_analysis.py`** run against the data as written.

## Key Concepts Demonstrated

- `groupby()` with a single aggregation and sorting
- Named aggregations via `.agg(name=("col", "func"))` for multi-metric KPI tables
- `pivot_table()` with `fill_value`, `margins`, and a custom `aggfunc`
- Turning aggregated numbers into business insights and recommendations
