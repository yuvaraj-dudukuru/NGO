# 🛍️ Mini Challenge — "ShopNed": Explore the Orders Database

**Scenario.** You are a junior data analyst at **ShopNed**, an online store.
The management team gives you access to the customer and order database and asks
you to **explore it, run several analytical queries, and present business
insights** — using only `SELECT`, `WHERE`, and `ORDER BY`.

---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `shopned_analysis.sql` | Fully commented SQL that creates the database, runs every required query, and includes the optional stretch goals. |
| `README.md` | This file — the explanation, findings and business report. |

---

## ▶️ How to run

The script is self-contained: it creates the `orders` table, inserts the data,
then runs the analysis. Pick whichever fits your setup:

1. With the SQLite command line:
   ```bash
   sqlite3 < shopned_analysis.sql
   ```
2. From Python / a Jupyter notebook (the brief's approach — `:memory:` database):
   ```python
   import sqlite3, pandas as pd
   conn = sqlite3.connect(":memory:")
   conn.executescript(open("shopned_analysis.sql").read())
   # then inspect any query as a DataFrame, e.g.:
   print(pd.read_sql("SELECT * FROM orders ORDER BY Amount DESC", conn))
   ```
3. Or
    ```bash
    Get-Content shopned_analysis.sql | sqlite3 
  
    or

    Get-Content shopned_analysis.sql | sqlite3 > results.txt
   ```

> **No data file needed** — the rows are created by the script itself.

---

## 📊 The dataset

The `orders` table records one row per order:

| Column | Meaning |
|--------|---------|
| `OrderID` | Unique order number (primary key) |
| `Customer` | Name of the customer (text) |
| `City` | City the order came from (text) |
| `Product` | Product purchased (text) |
| `Amount` | Order value in ₹ (numeric) |
| `OrderDate` | Date of the order, `'YYYY-MM-DD'` (text) |

```
+---------+----------+--------+--------+--------+------------+
| OrderID | Customer | City   | Product| Amount | OrderDate  |
+---------+----------+--------+--------+--------+------------+
| 1       | Asha     | Pune   | Laptop | 65000  | 2026-05-02 |
| 2       | Ravi     | Mumbai | Phone  | 30000  | 2026-05-03 |
| 3       | Imran    | Pune   | Mouse  | 1200   | 2026-05-05 |
| 4       | Divya    | Delhi  | Laptop | 60000  | 2026-05-06 |
| 5       | Karan    | Mumbai | Tablet | 20000  | 2026-05-08 |
| 6       | Meena    | Delhi  | Phone  | 30000  | 2026-05-09 |
| 7       | Sahil    | Pune   | Laptop | 70000  | 2026-05-11 |
| 8       | Tara     | Mumbai | Watch  | 8000   | 2026-05-12 |
+---------+----------+--------+--------+--------+------------+
```

---

## 🔍 What the script does, step by step

### 1. Explore the table (`SELECT *`)
```sql
SELECT * FROM orders;
```
Reveals **8 orders across 3 cities** (Pune, Mumbai, Delhi).

### 2. Retrieve specific data
```sql
SELECT Customer, Product, Amount FROM orders;
```

### 3. Apply filters
| Goal | Query |
|------|-------|
| Orders above ₹25,000 | `WHERE Amount > 25000` |
| Orders from Pune | `WHERE City = 'Pune'` |
| Pune Laptops above ₹50,000 | `WHERE City = 'Pune' AND Product = 'Laptop' AND Amount > 50000` |
| Orders from Mumbai or Delhi | `WHERE City = 'Mumbai' OR City = 'Delhi'` |

### 4. Sort results (highest first)
```sql
SELECT * FROM orders ORDER BY Amount DESC;
```
Top order: **Sahil's Laptop (₹70,000)** in Pune.

### 5. Combine SELECT + WHERE + ORDER BY
```sql
SELECT Customer, Product, Amount
FROM orders
WHERE Amount > 20000
ORDER BY Amount DESC;
```
Output:
```
Customer | Product | Amount
---------+---------+-------
Sahil    | Laptop  | 70000
Asha     | Laptop  | 65000
Divya    | Laptop  | 60000
Ravi     | Phone   | 30000
Meena    | Phone   | 30000
```

---

## ✅ Business insights & recommendations

> Each insight climbs the storytelling ladder: *observation → meaning → action.*

1. **Laptops are the key revenue driver.** The three highest-value orders are
   all Laptops, topped by Sahil's ₹70,000 sale.
   - 💡 **Recommendation:** Focus **laptop promotions** and keep premium
     electronics well stocked.

2. **Pune is a strong premium-electronics market** — it produces several
   high-value laptop sales (Asha ₹65,000, Sahil ₹70,000).
   - 💡 **Recommendation:** Concentrate **premium campaigns in Pune**.

3. **Orders above ₹25,000 are mostly Laptops and Phones** — the core revenue
   drivers. Mumbai and Delhi contribute several mid-value orders.
   - 💡 **Recommendation:** Stock more high-value electronics, and target
     **Mumbai and Delhi** for growth campaigns to lift their order values.

---

## 🚀 Stretch goals (optional)

The script ends with four optional blocks:

1. **`BETWEEN`** — orders placed between `'2026-05-05'` and `'2026-05-10'`.
2. **`LIKE`** — customers whose names start with a chosen letter (`'A%'`).
3. **Multi-column sort** — `ORDER BY City ASC, Amount DESC` in a single query.
4. **Pandas + Seaborn** — load a query result into a DataFrame and draw a bar
   chart of amount by product (combining Days 8 and 9).

---

## 🧠 Concepts practised
`SELECT *` · specific-column selection · numeric `WHERE` · text `WHERE` ·
`AND` · `OR` · `ORDER BY ... DESC` · combined `SELECT → WHERE → ORDER BY` ·
`BETWEEN` · `LIKE` · multi-column sort · turning query results into business
storytelling
