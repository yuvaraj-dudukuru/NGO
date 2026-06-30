# Advanced Practice — Sales EDA Report

**Analyst:** Jordan Lee  |  **Date:** 27 June 2026  |  **Data:** `sales_clean.csv`

## 1. Executive Summary

A messy 12-row sales export was cleaned to **11 valid orders** and analyzed end to end. The
analysis shows **Electronics dominates revenue (₹165,500 — ~90% of the total)** from a few large
orders, while Grocery and Clothing contribute little. **Pune is overwhelmingly the top-revenue
market (₹163,700)** because all the big Electronics orders are placed there. Two data-entry errors
(an amount of ₹888,888 and a quantity of −4) were detected and corrected. We recommend protecting
Electronics inventory, focusing on Pune, using Grocery to drive footfall, and adding data-entry
validation.

## 2. Business Problem

Clean a messy sales export and answer: which categories and cities drive revenue, who are the
high-value customers, and is the data trustworthy?

## 3. Dataset Description

- **Raw:** 12 rows × 7 columns (OrderID, Customer, City, Category, Amount, Quantity, OrderDate)
- **Clean:** **11 unique orders** (1 duplicate removed) — `sales_clean.csv`
- **Period:** 1–10 May 2026

## 4. Data Cleaning Summary

| Issue | Fix |
|-------|-----|
| Duplicate (OrderID 404) | `drop_duplicates(subset=["OrderID"])` |
| OrderDate as text | `pd.to_datetime()` |
| Messy text/case | `.str.strip().str.title()` |
| Invalid quantity (−4) | median of valid quantities |
| Outlier amount (888,888) | IQR-flagged (fence ≈ ₹129,313) → median fill |
| Missing amount (OrderID 409) | median fill |

**Result:** 0 missing, 0 duplicates, all quantities positive, correct types.

## 5. Key Findings

1. **Electronics = ₹165,500** revenue, vs Clothing ₹10,400 and Grocery ₹8,600 (~90% of total).
2. **Pune = ₹163,700** revenue, far ahead of Mumbai and Delhi (₹10,400 each) — driven entirely by
   Electronics orders located in Pune.
3. **Quantity ↔ Amount correlation = −0.64** — buying more units goes with *lower* spend (bulk
   Grocery vs single-unit Electronics): two distinct buying patterns.
4. **High-value customers** (all Electronics): Neha ₹60,000, Tina ₹55,000, Amit ₹47,000.
5. **Two data-quality errors** (₹888,888 amount, −4 quantity) reveal weak input validation.

## 6. Visualizations

Saved at dpi=300 in [`charts/`](charts/):
`01_revenue_by_category.png`, `02_amount_distribution.png`, `03_amount_by_category_box.png`,
`04_quantity_vs_amount.png`, `05_correlation_heatmap.png`.

## 7. Recommendations

1. **Protect Electronics inventory** — it is ~90% of revenue from a handful of orders.
2. **Prioritize Pune** for premium/Electronics promotions; it is the high-value market.
3. **Use Grocery as a footfall driver**, then upsell to Electronics.
4. **Add entry-side validation** (range checks on Amount and Quantity) to stop errors like
   ₹888,888 and −4 at the source.

## 8. Conclusion

After cleaning, the story is clear: **revenue is concentrated in high-value Electronics and the
Pune market**, while other categories/cities drive volume. Acting on these recommendations should
grow both revenue and data quality.
