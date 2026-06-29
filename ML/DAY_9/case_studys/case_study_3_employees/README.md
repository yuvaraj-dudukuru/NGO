# Case Study 3 — Employee Database Analysis 💼

A SQL mini-analysis of a small `employees` table. HR wants to **review salaries
by department**, and we answer that with `SELECT`, `WHERE`, and `ORDER BY`. It
combines text filtering, numeric filtering, and ranking — the everyday toolkit
of a people-analytics query.

---

## 📂 Files in this folder

| File | What it is |
|------|------------|
| `employees_analysis.sql` | Fully commented SQL that builds the table and runs every query below. |
| `README.md` | This file — the explanation and findings. |

---

## ▶️ How to run

The script is self-contained (it creates the table, inserts the data, then queries it).

1. With the SQLite command line:
   ```bash
   sqlite3 < employees_analysis.sql
   ```
2. Or from Python (matches the Day 9 hands-on activity):
   ```python
   import sqlite3
   conn = sqlite3.connect(":memory:")
   conn.executescript(open("employees_analysis.sql").read())
   ```
3. Or
   ```bash
   Get-Content employees_analysis.sql | sqlite3 
   
   or
   
   Get-Content employees_analysis.sql | sqlite3 > results.txt
   ```

---

## 📊 The data

```
EMPLOYEES
+-------+--------+------------+--------+
| EmpID | Name   | Department | Salary |
+-------+--------+------------+--------+
| 1     | Asha   | IT         | 50000  |
| 2     | Ravi   | HR         | 55000  |
| 3     | Imran  | IT         | 40000  |
| 4     | Divya  | Finance    | 90000  |
| 5     | Karan  | IT         | 60000  |
+-------+--------+------------+--------+
```
Primary key: `EmpID`.

---

## 🔍 What the script does, step by step

### 1. Filter — IT department, ranked by salary (text `WHERE` + `ORDER BY DESC`)
```sql
SELECT name, salary
FROM employees
WHERE department = 'IT'
ORDER BY salary DESC;
```
Output:
```
Name  | Salary
------+-------
Karan | 60000
Asha  | 50000
Imran | 40000
```
- **Interpretation:** Among IT staff, Karan is the highest paid and Imran the
  lowest — useful for **pay-equity reviews**.

### 2. Filter — high earners across the company (numeric `WHERE` + `ORDER BY DESC`)
```sql
SELECT name, department, salary
FROM employees
WHERE salary > 50000
ORDER BY salary DESC;
```
Output:
```
Name  | Department | Salary
------+------------+-------
Divya | Finance    | 90000
Karan | IT         | 60000
Ravi  | HR         | 55000
```
- **Interpretation:** Three employees earn above ₹50,000, led by Divya in
  Finance.

---

## ✅ Findings and recommendations

- Within **IT**, salaries range from ₹40,000 (Imran) to ₹60,000 (Karan) — a
  clear spread for a pay-equity review.
- Company-wide, **three employees** earn above ₹50,000, led by **Divya
  (Finance, ₹90,000)**.
- **Recommendation:** This filtered, ranked view supports budget planning and
  identifies senior staff — the same finding as the Day 6/8 employee analyses,
  now produced directly from the database with SQL.

---

## 🧠 Concepts practised
`WHERE` on text (`department = 'IT'`) · `WHERE` on numbers (`salary > 50000`) ·
`ORDER BY ... DESC` for ranking · reading an HR insight from a ranked result
