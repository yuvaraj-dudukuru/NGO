# Day 11 — Advanced Pandas: Hands-On Activity

A complete multi-table analysis performed end-to-end: grouping, multiple aggregations,
merging, pivot tables, crosstabs, and KPI reporting — **the complete advanced pandas
toolkit, working on multiple tables together.**

## Files

| File | Description |
|------|-------------|
| `Day11_Advanced_Pandas.ipynb` | The Jupyter notebook (9 steps as cells, outputs included) |
| `day11_advanced_pandas.py` | Plain-Python mirror of the same 8 code steps |
| `README.md` | This document |

## Requirements

- Python 3.8+
- pandas
- (Notebook only) Jupyter / JupyterLab or VS Code with the Jupyter extension

```bash
pip install pandas jupyter
```

## How to Run

**Notebook**

```bash
jupyter notebook Day11_Advanced_Pandas.ipynb
```

Then run all cells (Kernel → Restart & Run All), or open it in VS Code.

**Script**

```bash
python day11_advanced_pandas.py
```

## The Data

**customers**

| CustomerID | Name  | City   |
|-----------:|-------|--------|
| 1 | Asha  | Pune   |
| 2 | Ravi  | Mumbai |
| 3 | Imran | Pune   |
| 4 | Divya | Delhi  |

**orders**

| OrderID | CustomerID | Category | Amount |
|--------:|-----------:|----------|-------:|
| 101 | 1 | Elec  | 25000 |
| 102 | 2 | Groc  |  1500 |
| 103 | 1 | Elec  | 30000 |
| 104 | 3 | Cloth |  9000 |
| 105 | 4 | Groc  |  2000 |

## The 9 Steps

### Step 1 — Load multiple datasets
Build the `customers` and `orders` DataFrames.

### Step 2 — GroupBy analysis

```python
orders.groupby("Category")["Amount"].sum()
```

```
Category
Cloth     9000
Elec     55000
Groc      3500
Name: Amount, dtype: int64
```

### Step 3 — Multiple aggregations

```python
orders.groupby("Category").agg(
    Total=("Amount", "sum"), Average=("Amount", "mean"), Count=("Amount", "count")
).reset_index()
```

```
  Category  Total  Average  Count
0    Cloth   9000   9000.0      1
1     Elec  55000  27500.0      2
2     Groc   3500   1750.0      2
```

### Step 4 — Merge tables

```python
merged = pd.merge(orders, customers, on="CustomerID", how="left")
```

```
   OrderID  CustomerID Category  Amount   Name    City
0      101           1     Elec   25000   Asha    Pune
1      102           2     Groc    1500   Ravi  Mumbai
2      103           1     Elec   30000   Asha    Pune
3      104           3    Cloth    9000  Imran    Pune
4      105           4     Groc    2000  Divya   Delhi
```

### Step 5 — Analyze the merged (multi-table) data

```python
merged.groupby("City")["Amount"].sum().sort_values(ascending=False)
```

```
City
Pune      64000
Delhi      2000
Mumbai     1500
Name: Amount, dtype: int64
```

### Step 6 — Pivot table

```python
pd.pivot_table(merged, index="City", columns="Category",
               values="Amount", aggfunc="sum", fill_value=0, margins=True)
```

```
Category  Cloth   Elec  Groc    All
City
Delhi         0      0  2000   2000
Mumbai        0      0  1500   1500
Pune       9000  55000     0  64000
All        9000  55000  3500  67500
```

### Step 7 — KPI report

```python
merged.groupby("City").agg(
    Total_Revenue=("Amount", "sum"), Orders=("OrderID", "count")
).reset_index().sort_values("Total_Revenue", ascending=False)
```

```
     City  Total_Revenue  Orders
2    Pune          64000       3
0   Delhi           2000       1
1  Mumbai           1500       1
```

### Step 8 — Crosstab analysis

```python
pd.crosstab(merged["City"], merged["Category"])
```

```
Category  Cloth  Elec  Groc
City
Delhi         0     0     1
Mumbai        0     0     1
Pune          1     2     0
```

### Step 9 — Document insights

- **Pune dominates revenue** (₹64,000 from 3 orders), driven by Electronics.
- **Electronics is the top category** (₹55,000), concentrated in Pune.
- **Mumbai and Delhi contribute little** — growth opportunities.
- **Recommendation:** Focus on Pune and Electronics; investigate Mumbai/Delhi.

> All outputs above were **verified** by running the code — they match the activity's
> expected output exactly.

## Key Concepts Demonstrated

| Technique | Step |
|-----------|------|
| GroupBy + single aggregation | 2, 5 |
| Multiple named aggregations | 3, 7 |
| Merging / joins (`pd.merge`) | 4 |
| Pivot tables (`pd.pivot_table`) | 6 |
| Crosstabs (`pd.crosstab`) | 8 |
| KPI reporting & ranking | 7 |
| Turning analysis into insights | 9 |
