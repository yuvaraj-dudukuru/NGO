# Case Study 1 — Customer Database Analysis 👥

A complete SQL mini-analysis of a small `customers` table. A retail company
wants to understand its customer base for a **marketing campaign**, and we
answer that using only `SELECT`, `WHERE`, and `ORDER BY`. This is the best
first case study because it introduces every clause you'll reuse in the others.

---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `customers_analysis.sql` | Fully commented SQL that builds the table and runs every query below. |
| `README.md` | This file — the explanation and findings. |

---

## ▶️ How to run

The script is self-contained (it creates the table, inserts the data, then queries it).

1. With the SQLite command line:
   ```bash
   sqlite3 < customers_analysis.sql
   ```
2. Or from Python (matches the Day 9 hands-on activity):
   ```python
   import sqlite3
   conn = sqlite3.connect(":memory:")
   conn.executescript(open("customers_analysis.sql").read())
   ```
3. Or 
   ```bash
   Get-Content customers_analysis.sql | sqlite3 
   
   or
   
   Get-Content customers_analysis.sql | sqlite3 > results.txt
   ```
---

## 📊 The data

```
CUSTOMERS
+------------+--------+-----------+-----+
| CustomerID | Name   | City      | Age |
+------------+--------+-----------+-----+
| 101        | Rajesh | Hyderabad | 28  |
| 102        | Priya  | Bengaluru | 34  |
| 103        | Aman   | Mumbai    | 22  |
| 104        | Sneha  | Delhi     | 41  |
| 105        | Karan  | Hyderabad | 30  |
+------------+--------+-----------+-----+
```
Primary key: `CustomerID`. 5 customers across 4 cities.

---

## 🔍 What the script does, step by step

### 1. Data retrieval — see the whole table (`SELECT *`)
```sql
SELECT * FROM customers;
```
- **Interpretation:** A quick first look, like `df.head()` in Pandas. We have
  5 customers across 4 cities (Hyderabad appears twice).

### 2. Filtering — target a specific city (`WHERE`)
```sql
SELECT name, age FROM customers WHERE city = 'Hyderabad';
```
- **Interpretation:** Two customers (Rajesh, Karan) are in Hyderabad — a target
  group for a local campaign. Note the **single quotes** around the text value.

### 3. Sorting — rank by age (`ORDER BY ... DESC`)
```sql
SELECT name, city, age FROM customers ORDER BY age DESC;
```
- **Interpretation:** The oldest customer is Sneha (41); the youngest is Aman
  (22). Knowing the age spread helps tailor messaging.

### 4. Combined analysis — older customers, sorted (`WHERE` + `ORDER BY`)
```sql
SELECT name, city, age
FROM customers
WHERE age >= 30
ORDER BY age DESC;
```
Output:
```
Name  | City      | Age
------+-----------+----
Sneha | Delhi     | 41
Priya | Bengaluru | 34
Karan | Hyderabad | 30
```
- **Interpretation:** Three customers are 30 or older, ranked oldest first.

---

## ✅ Findings and recommendations

- The database has **5 customers** across **4 cities**.
- **Two customers (Rajesh, Karan)** are in Hyderabad — a ready-made list for a
  local campaign.
- **Sneha (41)** is the oldest customer; **Aman (22)** the youngest.
- **Recommendation:** For a premium product aimed at mature customers, the
  filtered + ranked list of three customers aged 30+ is exactly the target
  audience — a complete mini-analysis from one query.

---

## 🧠 Concepts practised
`SELECT *` · specific-column selection · `WHERE` on text (single quotes) ·
`ORDER BY ... DESC` · combining `SELECT → WHERE → ORDER BY`
