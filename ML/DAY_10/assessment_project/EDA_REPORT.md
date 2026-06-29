# FreshBasket Sales — Exploratory Data Analysis Report

**Analyst:** Jordan Lee  |  **Date:** 27 June 2026
**Dataset:** `freshbasket_clean.csv`  |  **Tools:** Python (Pandas, Matplotlib, Seaborn, SQLite)

---

## 1. Executive Summary

FreshBasket's recent sales export (10 raw orders) was cleaned and analyzed. After removing one
duplicate and correcting several data-quality issues, **9 valid orders** remained. The analysis
shows that **Electronics dominates revenue (₹135,000 — about 90% of the total)** from just three
large orders, while **Grocery and Clothing contribute very little** despite Grocery having the
most orders. **Pune is the highest-revenue city (₹135,000)** even though **Mumbai places the most
orders (4)**. One serious data-entry error (an order recorded as ₹999,999) was detected and
corrected. We recommend **protecting Electronics inventory, targeting Pune for high-value sales,
using Grocery to drive footfall, and adding data-entry validation.**

## 2. Business Problem

FreshBasket management asked for a complete analysis of a messy sales export: *Which cities and
categories drive revenue? Who are the top customers? Is anything unusual in the data?* The goal is
to guide inventory and marketing decisions.

## 3. Dataset Description

| Property | Value |
|----------|-------|
| Source | FreshBasket sales export (raw) → `freshbasket_clean.csv` |
| Period | 1–8 May 2026 |
| Raw size | 10 rows × 7 columns |
| Clean size | **9 unique orders** × 7 columns (1 duplicate removed) |
| Columns | OrderID, Customer, City, Category, Amount, Quantity, OrderDate |

## 4. Data Cleaning Summary

| Issue found | Fix applied |
|-------------|-------------|
| Duplicate order (OrderID 203) | `drop_duplicates(subset=["OrderID"])` |
| OrderDate stored as text | `pd.to_datetime()` |
| Inconsistent text (`"  ravi"`, `"ASHA"`, `"meena "`, `"mumbai"`) | `.str.strip().str.title()` |
| Invalid quantity (−3) | replaced with median of valid quantities (= 2) |
| Outlier amount (999,999) | flagged by IQR (fence ≈ ₹113,500) → treated as error → filled with median |
| Missing amount (OrderID 205) | filled with median (= ₹3,200) |

**Result:** a clean, validated dataset — **0 missing values, 0 duplicates, all quantities
positive, correct data types.**

## 5. Key Findings

1. **Electronics drives revenue.** Electronics = **₹135,000**, vs Grocery ₹9,100 and Clothing
   ₹5,700. Roughly **90% of all revenue** comes from Electronics.
2. **A few big orders carry the business.** The three high-value orders (₹52,000, ₹45,000,
   ₹38,000) are all Electronics and all in Pune.
3. **Top city depends on the metric.** **Pune leads revenue (₹135,000)**; **Mumbai leads order
   count (4 orders)**. They are two different kinds of "best" market.
4. **Grocery is volume, not value.** Grocery has the most orders (4) and the highest quantities
   but contributes little revenue.
5. **Quantity and Amount are negatively correlated (−0.62).** Buying *more* units tends to mean
   *lower* spend — cheap Grocery sells in bulk, pricey Electronics sells one at a time.
6. **A data-quality issue exists.** The ₹999,999 entry exposed weak input controls.

## 6. Visualizations

All charts saved at **dpi=300** in [`charts/`](charts/).

| Chart | File | Interpretation |
|-------|------|----------------|
| Bar — Revenue by Category | `01_revenue_by_category.png` | Electronics towers over Grocery & Clothing |
| Bar — Revenue by City | `02_revenue_by_city.png` | Pune is the revenue leader |
| Histogram — Order Amounts | `03_amount_distribution.png` | Most orders are small; a few large ones dominate revenue |
| Box plot — Amount by Category | `04_amount_by_category_box.png` | Electronics has the highest, widest spread |
| Scatter — Quantity vs Amount | `05_quantity_vs_amount.png` | Two buying patterns: high-qty/low-value vs low-qty/high-value |
| Heatmap — Correlation | `06_correlation_heatmap.png` | Quantifies the −0.62 Quantity↔Amount relationship |

## 7. Recommendations

1. **Protect Electronics inventory.** It produces ~90% of revenue from a handful of orders —
   a stockout here directly threatens the bottom line.
2. **Target Pune for high-value sales.** Pune's customers (Ravi, Imran, Sahil) are all
   high-value Electronics buyers; focus premium promotions there.
3. **Lift Mumbai's order value.** Mumbai has the most orders but low spend — use bundles and
   loyalty offers to raise average order value.
4. **Use Grocery as an acquisition channel.** It drives footfall; pair Grocery deals with
   Electronics upsells.
5. **Add data-entry validation.** Range checks on Amount and Quantity would have blocked the
   ₹999,999 and −3 errors at the source.

## 8. Conclusion

After cleaning, the data tells a clear story: **revenue is concentrated in high-value Electronics
and in the Pune market**, while Grocery and Mumbai drive volume rather than value. Acting on these
recommendations — protecting Electronics stock, targeting Pune, monetizing Grocery footfall, and
tightening data entry — should improve both revenue and data quality.
