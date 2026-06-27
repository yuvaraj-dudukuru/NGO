# ShopEasy Sales — Mini Challenge

**Role:** Junior Data Analyst
**Brief:** "I feel like something is off with our data, and I want to understand our customers better. Can you take a look?" — Marketing Manager
**Dataset:** `shopeasy_sales.csv`

---

## Raw Dataset

| OrderID | Customer | City    | Category    | Price  | Quantity | OrderDate  | Rating |
|---------|----------|---------|-------------|--------|----------|------------|--------|
| 2001    | Asha     | Pune    | Electronics | 15000  | 1        | 2026-05-10 | 4.6    |
| 2002    | Neha     | Pune    | Clothing    | 1200   | 3        | 2026-05-10 | 4.2    |
| 2003    | Imran    | Kolkata | Electronics | 15000  | 1        | 2026-05-11 | *(blank)* |
| 2004    | Asha     | pune    | Books       | 499    | 2        | 2026-05-11 | 4.9    |
| 2005    | Ravi     | Chennai | Clothing    | 1500   | -2       | 2026-05-12 | 3.5    |
| 2006    | Neha     | Pune    | Electronics | 250000 | 1        | 2026-05-12 | 4.0    |
| 2007    | Imran    | Kolkata | Books       | 650    | 1        | 2026-05-13 | 4.4    |
| 2008    | Divya    | Chennai | Clothing    | 1800   | 2        | 2026-05-13 | 4.7    |
| 2008    | Divya    | Chennai | Clothing    | 1800   | 2        | 2026-05-13 | 4.7    |
| 2010    | Ravi     | Chennai | Electronics | 30000  | 1        | 2026-05-14 | 4.1    |

> 🔎 Highlighted issues are visible directly in the table: blank rating (2003), lowercase `pune` (2004), negative quantity (2005), extreme price (2006), duplicated row (2008), and a missing OrderID 2009.

---

## 1. Dataset Structure

- **Rows:** 10 data rows, but only **9 unique orders** (one is duplicated).
- **Columns:** 8

| Column    | Data Type              | Notes |
|-----------|------------------------|-------|
| OrderID   | Identifier (integer)   | A label, not for math |
| Customer  | Text / categorical     | |
| City      | Categorical            | |
| Category  | Categorical            | |
| Price     | Numerical (continuous) | |
| Quantity  | Numerical (discrete)   | whole units |
| OrderDate | Date                   | |
| Rating    | Numerical (continuous) | scale ~1–5 |

---

## 2. Five Business Questions

1. Which **product category** generates the most revenue (Price × Quantity)?
2. Which **cities** are most active by orders and by revenue?
3. Who are our **repeat customers**, and what do they buy?
4. Is **customer satisfaction** (average Rating) consistent across categories/cities?
5. How are **sales trending day-by-day** over the period?

---

## 3. Data-Quality Problems & Fixes

| # | Row(s) | Problem | Proposed Fix |
|---|--------|---------|--------------|
| 1 | 2008 | **Duplicate record** — Divya's order appears twice | Drop the duplicate row |
| 2 | 2003 | **Missing value** — blank Rating | Follow up with customer; or impute (e.g., category mean) and flag |
| 3 | 2004 | **Inconsistent format** — city `pune` vs `Pune` | Standardize casing (title-case all cities) |
| 4 | 2005 | **Impossible value** — Quantity = `-2` | Correct to `2` if a sign error, else remove/verify |
| 5 | 2006 | **Outlier** — Price `250,000` (≈10× the next highest) | Investigate; likely an extra-zero typo — verify before averaging |
| 6 | 2009 | **Gap in sequence** — no OrderID 2009 | Minor; an order may be missing from the export |

> ⚠️ The duplicate (#1) and the outlier (#5) both **distort averages and revenue totals** if not handled first.

---

## 4. Descriptive Insights (after cleaning)

- **Electronics drives revenue.** Even excluding the suspicious ₹250,000 row, single Electronics orders (₹15,000–₹30,000) dwarf Clothing and Books (₹499–₹1,800).
- **Pune and Chennai are the most active cities**, with Kolkata behind.
- **Customers are generally happy.** Valid ratings range ~3.5–4.9, mostly above 4.0 — strong satisfaction (ignoring the one missing rating).
- **Repeat customers exist:** Asha, Neha, Imran, and Ravi each ordered more than once — worth nurturing for loyalty.

---

## 5. Note to the Marketing Manager

> I reviewed the sample data and you were right — a few things need cleaning before we trust the numbers. There's one duplicated order, a missing customer rating, an impossible negative quantity, an inconsistently typed city name, and one unusually high price that looks like a typo and should be verified. After fixing these, the early picture is encouraging: **Electronics is our top revenue driver, Pune and Chennai are our busiest cities, and customer ratings are strong (mostly above 4.0).** Once I finalize the cleaned dataset, I can give you a reliable breakdown of sales by city and category to guide where we focus marketing spend.
