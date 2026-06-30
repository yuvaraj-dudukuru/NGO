# Mini Challenge — ShopVerse Multi-Table Business Analysis

**Role:** Senior data analyst at *ShopVerse*, a multi-category online retailer.
**Task:** Combine three related tables into one analysis dataset and produce a complete
business analysis — pivot tables, KPI reports, a crosstab, and actionable insights.

This is the capstone of Day 11: it uses **every** technique from the day —
multi-table joins, feature engineering, pivot tables, GroupBy KPIs, `idxmax`, and
crosstabs — on three tables at once.

## Files

| File | Description |
|------|-------------|
| `shopverse_analysis.py` | Full solution: requirements 1–4 + stretch goals |
| `revenue_by_city.png` | Stretch goal — Seaborn bar chart of revenue by city |
| `README.md` | This document |

## Requirements

- Python 3.8+
- pandas
- *(stretch chart only)* matplotlib, seaborn

```bash
pip install pandas matplotlib seaborn
```

## How to Run

```bash
python shopverse_analysis.py
```

The chart step is optional and self-guards: if matplotlib/seaborn aren't installed it
prints a notice and skips, instead of crashing.

## The Three Tables

**customers**

| CustomerID | Name | City | Segment |
|---:|---|---|---|
| 1 | Asha  | Pune   | Premium |
| 2 | Ravi  | Mumbai | Regular |
| 3 | Imran | Pune   | Premium |
| 4 | Divya | Delhi  | Regular |
| 5 | Karan | Mumbai | Premium |

**products**

| ProductID | Product | Category | Price |
|---|---|---|---:|
| P1 | Laptop     | Electronics | 60000 |
| P2 | Phone      | Electronics | 30000 |
| P3 | Headphones | Accessories |  3000 |

**orders**

| OrderID | CustomerID | ProductID | Quantity |
|---:|---:|---|---:|
| 101 | 1 | P1 | 1 |
| 102 | 2 | P2 | 2 |
| 103 | 1 | P3 | 3 |
| 104 | 3 | P1 | 1 |
| 105 | 4 | P2 | 1 |
| 106 | 5 | P1 | 1 |
| 107 | 1 | P2 | 2 |
| 108 | 3 | P3 | 5 |

## 1. Merge + Revenue column

```python
step1 = pd.merge(orders, customers, on="CustomerID", how="left")
full  = pd.merge(step1, products, on="ProductID", how="left")
full["Revenue"] = full["Quantity"] * full["Price"]
```

```
   OrderID   Name    City  Segment     Product     Category  Quantity  Price  Revenue
0      101   Asha    Pune  Premium      Laptop  Electronics         1  60000    60000
1      102   Ravi  Mumbai  Regular       Phone  Electronics         2  30000    60000
2      103   Asha    Pune  Premium  Headphones  Accessories         3   3000     9000
3      104  Imran    Pune  Premium      Laptop  Electronics         1  60000    60000
4      105  Divya   Delhi  Regular       Phone  Electronics         1  30000    30000
5      106  Karan  Mumbai  Premium      Laptop  Electronics         1  60000    60000
6      107   Asha    Pune  Premium       Phone  Electronics         2  30000    60000
7      108  Imran    Pune  Premium  Headphones  Accessories         5   3000    15000
```

**Total revenue = ₹354,000.**

## 2. Pivot Tables

**2a. Revenue by City × Category (with totals)**

```
Category  Accessories  Electronics     All
City
Delhi               0        30000   30000
Mumbai              0       120000  120000
Pune            24000       180000  204000
All             24000       330000  354000
```

**2b. Revenue by Segment × Product**

```
Product  Headphones  Laptop  Phone
Segment
Premium       24000  180000  60000
Regular           0       0  90000
```

## 3. KPI Reports

**3a. Total revenue by city (descending)**

```
City
Pune      204000
Mumbai    120000
Delhi      30000
```

**3b. Total revenue by segment**

```
Segment
Premium    264000
Regular     90000
```

**3c. Top customer by total revenue** (`idxmax()`) → **Asha** (₹129,000)

**3d. Total revenue by product category**

```
Category
Accessories     24000
Electronics    330000
```

## 4. Crosstab — order count by City × Category

```
Category  Accessories  Electronics
City
Delhi               0            1
Mumbai              0            2
Pune                2            3
```

## 5. Business Insights — climbing the Insight Ladder

Each finding climbs from **Observation → Insight → Recommendation**.

**Finding 1 — Electronics dominates, powered by Premium**
- *Observation:* Electronics = ₹330,000 of ₹354,000 (93%); Premium = ₹264,000 (75%).
- *Insight:* Revenue rests on high-value Electronics bought by a small Premium group.
- *Recommendation:* Launch a Premium loyalty program; prioritize Laptop/Electronics stock.

**Finding 2 — Pune is the revenue engine, led by Asha**
- *Observation:* Pune = ₹204,000 (58% of revenue); Asha alone = ₹129,000 across 3 orders.
- *Insight:* Revenue is geographically concentrated and customer-concentrated.
- *Recommendation:* Nurture top customers like Asha; double down on Pune (and Mumbai).

**Finding 3 — Accessories: high volume, low value**
- *Observation:* Headphones sold the most units (3 + 5 = 8) yet earned only ₹24,000.
- *Insight:* The classic high-volume / low-value pattern — units ≠ revenue.
- *Recommendation:* Use Accessories to drive footfall/volume and upsell Electronics.

**Stretch finding — Average order value is similar across segments**
- *Observation:* AOV ≈ ₹44,000 (Premium) vs ₹45,000 (Regular).
- *Insight:* Premium leads on *total* revenue through **order frequency** (6 orders), not
  bigger individual orders — Regulars place few but comparably sized orders.
- *Recommendation:* Grow Premium revenue by increasing purchase frequency; convert
  Regulars (esp. in Mumbai/Delhi) into repeat buyers.

## 6. Conclusions & Recommendations

ShopVerse revenue is concentrated on three fronts at once: **Electronics** (category),
**Premium** (segment), and **Pune** (city) — and they overlap heavily (Premium buyers in
Pune purchasing Laptops). This concentration is both a strength and a risk.

- **Launch a Premium loyalty program** — Premium drives 75% of revenue via repeat orders.
- **Prioritize Laptop / Electronics inventory** in Pune and Mumbai.
- **Nurture top customers** like Asha with personalized retention.
- **Use Accessories (Headphones)** as a volume/footfall driver and upsell to Electronics.
- **De-risk concentration** — grow Delhi and the Regular segment to broaden the base.

## Stretch Goals Completed

- ✅ **Seaborn bar chart** of revenue by city → `revenue_by_city.png`
- ✅ **Average order value per segment** (Premium ₹44,000 vs Regular ₹45,000)
- ✅ **EDA-style report** — the insight ladder + conclusions above

## Key Concepts Demonstrated

| Technique | Where |
|-----------|-------|
| Chained 3-table joins (`pd.merge`) | Req. 1 |
| Feature engineering (`Revenue` column) | Req. 1 |
| Pivot tables with `margins`/`fill_value` | Req. 2 |
| GroupBy KPI reports + `sort_values` | Req. 3 |
| `idxmax()` to find the top customer | Req. 3c |
| Crosstab order counts | Req. 4 |
| Insight ladder → recommendations | Req. 5–6 |
| Seaborn visualization + AOV (stretch) | Stretch |
