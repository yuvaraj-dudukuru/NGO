# Case Study 2 — Sales Database Analysis 🛒

A SQL mini-analysis of a small `orders` table. A sales manager wants to
**review recent high-value orders**, and we answer that with `SELECT`, `WHERE`,
and `ORDER BY`. This case study adds **numeric filtering** and **date-range
filtering** to the skills from Case Study 1.

---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `sales_analysis.sql` | Fully commented SQL that builds the table and runs every query below. |
| `README.md` | This file — the explanation and findings. |

---

## ▶️ How to run

The script is self-contained (it creates the table, inserts the data, then queries it).

1. With the SQLite command line:
   ```bash
   sqlite3 < sales_analysis.sql
   ```
2. Or from Python (matches the Day 9 hands-on activity):
   ```python
   import sqlite3
   conn = sqlite3.connect(":memory:")
   conn.executescript(open("sales_analysis.sql").read())
   ```
3. Or
   ```bash
   Get-Content sales_analysis.sql | sqlite3 
   
   or
   
   Get-Content sales_analysis.sql | sqlite3 > results.txt
   ```

---

## 📊 The data

```
ORDERS
+---------+------------+---------+--------+------------+
| OrderID | CustomerID | Product | Amount | OrderDate  |
+---------+------------+---------+--------+------------+
| 5001    | 101        | Laptop  | 60000  | 2026-06-01 |
| 5002    | 102        | Phone   | 30000  | 2026-06-02 |
| 5003    | 101        | Mouse   | 1200   | 2026-06-03 |
| 5004    | 103        | Tablet  | 20000  | 2026-06-05 |
| 5005    | 104        | Phone   | 30000  | 2026-06-07 |
+---------+------------+---------+--------+------------+
```
Primary key: `OrderID`. Foreign key: `CustomerID` (links to the customers table).

---

## 🔍 What the script does, step by step

### 1. Retrieve all orders (specific columns)
```sql
SELECT OrderID, Product, Amount, OrderDate FROM orders;
```
- **Interpretation:** Listing the needed columns (instead of `SELECT *`) is the
  cleaner, report-ready habit.

### 2. Filter — high-value orders only (numeric `WHERE` + `ORDER BY DESC`)
```sql
SELECT Product, Amount
FROM orders
WHERE Amount > 25000
ORDER BY Amount DESC;
```
Output:
```
Product | Amount
--------+-------
Laptop  | 60000
Phone   | 30000
Phone   | 30000
```
- **Interpretation:** The Laptop is the single highest-value sale; Phones appear
  twice as strong contributors. Numbers take **no quotes**.

### 3. Filter by date — this week's orders (`BETWEEN` + `ORDER BY ASC`)
```sql
SELECT OrderID, Product, Amount, OrderDate
FROM orders
WHERE OrderDate BETWEEN '2026-06-01' AND '2026-06-05'
ORDER BY OrderDate ASC;
```
Output:
```
OrderID | Product | Amount | OrderDate
--------+---------+--------+-----------
5001    | Laptop  | 60000  | 2026-06-01
5002    | Phone   | 30000  | 2026-06-02
5003    | Mouse   | 1200   | 2026-06-03
5004    | Tablet  | 20000  | 2026-06-05
```
- **Interpretation:** Dates use **quotes** in `'YYYY-MM-DD'` format, and
  `BETWEEN` is inclusive of both ends — exactly how an analyst pulls "this
  week's" orders.

---

## ✅ Findings and recommendations

- The **Laptop (₹60,000)** is the single highest-value sale.
- **Phones** appear twice and are strong revenue contributors.
- Early-June orders are **dominated by electronics**.
- **Recommendation:** The manager can confidently report that high-value
  electronics drive early-month revenue, and plan stock accordingly.

---

## 🧠 Concepts practised
Specific-column selection · numeric `WHERE` (no quotes) · `ORDER BY ... DESC` ·
date filtering with `BETWEEN` (quoted `'YYYY-MM-DD'`) · `ORDER BY ... ASC`
