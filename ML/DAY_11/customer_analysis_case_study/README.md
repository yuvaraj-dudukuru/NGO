# Business Analytics Case Study 2 — Customer Analysis

A hands-on case study using **merging (joins)** to combine customer and order tables,
then applying **GroupBy** for customer segmentation and revenue analysis.

## Files

| File | Description |
|------|-------------|
| `customer_analysis.py` | Runnable script with both tables and all three analyses |
| `README.md` | This document |

## Requirements

- Python 3.8+
- pandas

```bash
pip install pandas
```

## How to Run

```bash
python customer_analysis.py
```

## The Tables

**customers**

| CustomerID | Name  | City   | Segment |
|-----------:|-------|--------|---------|
| 1 | Asha  | Pune   | Premium |
| 2 | Ravi  | Mumbai | Regular |
| 3 | Imran | Pune   | Premium |
| 4 | Divya | Delhi  | Regular |

**orders**

| OrderID | CustomerID | Amount |
|--------:|-----------:|-------:|
| 101 | 1 | 25000 |
| 102 | 2 |  1500 |
| 103 | 1 | 30000 |
| 104 | 3 | 18000 |
| 105 | 4 |  2000 |
| 106 | 1 | 12000 |

## Analyses

### 1. Merge — Join Orders to Customer Details

A left join attaches each order to its customer's name, city, and segment:

```python
merged = pd.merge(orders, customers, on="CustomerID", how="left")
```

### 2. Total Spending by Customer

```python
merged.groupby("Name")["Amount"].sum().sort_values(ascending=False)
```

```
Name
Asha     67000
Imran    18000
Divya     2000
Ravi      1500
Name: Amount, dtype: int64
```

### 3. Revenue by Segment

```python
merged.groupby("Segment")["Amount"].sum()
```

```
Segment
Premium    85000
Regular     3500
Name: Amount, dtype: int64
```

### 4. Revenue by City

```python
merged.groupby("City")["Amount"].sum()
```

```
City
Delhi      2000
Mumbai     1500
Pune      85000
Name: Amount, dtype: int64
```

## Insights and Recommendations

- **Finding:** Asha is by far the top customer (₹67,000 across three orders).
- **Finding:** Premium customers generate ₹85,000 vs. just ₹3,500 from Regular — the
  Premium segment drives almost all revenue.
- **Insight:** A small group of premium customers (concentrated in Pune, ₹85,000)
  accounts for the vast majority of revenue.
- **Recommendation:**
  - Launch a loyalty program for Premium customers.
  - Focus retention efforts on top spenders like Asha.
  - Design campaigns to convert Regular customers to Premium.

> This insight was only possible by **merging** the customer and order tables —
> neither table alone could reveal it. The `orders` table has the amounts but no
> segment/city; the `customers` table has the attributes but no spend.

> **Note on the source figures:** In the original brief, the "Total spending by
> customer" list was not actually sorted descending (it placed Ravi ₹1,500 above
> Divya ₹2,000), and the "Revenue by city" rows were in a different order. The output
> above is the **verified result of `customer_analysis.py`**. Note that
> `groupby(...).sum()` returns results sorted by the group key (so the city table is
> alphabetical: Delhi, Mumbai, Pune) unless you explicitly call `.sort_values()`.

## Key Concepts Demonstrated

- `pd.merge(..., how="left")` to combine related tables on a key
- GroupBy aggregation over the merged result
- `.sort_values(ascending=False)` for ranking customers
- Default group-key ordering of `groupby().sum()`
- Translating a join + aggregation into segmentation strategy
