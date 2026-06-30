# 🗄️ Case Studies — SQL for Data Analysis (SELECT · WHERE · ORDER BY)

Welcome! This folder contains **three complete, real-world style case studies**
that bring together the SQL skills learned on Day 9. Each case study takes a
small database table, asks a business question about it, and answers it with
plain **SQL queries** — using only the three core commands you learned today:
`SELECT`, `WHERE`, and `ORDER BY`.

These are the SQL versions of the kind of analyses you did in Pandas on Day 8 —
now produced directly from a database.

---

## 🗂️ Folder structure

```
case_studys/
│
├── README.md                          ← you are here (overview of everything)
│
├── case_study_1_customers/
│   ├── customers_analysis.sql         ← commented SQL (setup + queries)
│   └── README.md                      ← explanation + findings
│
├── case_study_2_sales/
│   ├── sales_analysis.sql             ← commented SQL (setup + queries)
│   └── README.md                      ← explanation + findings
│
└── case_study_3_employees/
    ├── employees_analysis.sql         ← commented SQL (setup + queries)
    └── README.md                      ← explanation + findings
```

---

## 📚 The three case studies

| # | Case study | Table | Main question | Key SQL |
|---|------------|-------|---------------|---------|
| 1 | **Customer Database** 👥 | `customers` | Who do we target for a marketing campaign? | `SELECT *`, `WHERE`, `ORDER BY` |
| 2 | **Sales Database** 🛒 | `orders` | What are our recent high-value orders? | `WHERE Amount >`, `BETWEEN`, `ORDER BY DESC` |
| 3 | **Employee Database** 💼 | `employees` | How do salaries compare by department? | `WHERE department =`, `ORDER BY salary DESC` |

Open each sub-folder's `README.md` for the full write-up of that case study.

---

## ▶️ How to run any case study

Each `.sql` file is **self-contained** — it creates the table, inserts the data,
then runs the analysis queries. You only need a SQL engine. The easiest is
**SQLite**, which ships with Python (no install needed).

**Option A — SQLite command line:**
```bash
sqlite3 < customers_analysis.sql
```

**Option B — From Python (matches the Day 9 hands-on activity):**
```python
import sqlite3
conn = sqlite3.connect(":memory:")
with open("customers_analysis.sql") as f:
    conn.executescript(f.read())
```

**Option C — Paste the queries** into any SQL tool (DB Browser for SQLite,
MySQL Workbench, PostgreSQL `psql`, an online SQL playground). The core
`SELECT / WHERE / ORDER BY` syntax is identical across all of them.

---

## 🧰 What's inside each `.sql` file

| Part | Why it's there |
|------|----------------|
| `DROP TABLE IF EXISTS` | Lets you re-run the script cleanly without errors. |
| `CREATE TABLE` | Defines the columns and the primary key. |
| `INSERT INTO` | Loads the sample rows (the same data from the Day 9 notes). |
| `SELECT … WHERE … ORDER BY` | The actual analysis — one query per business question. |
| `-- comments` | Explain each query and state the insight it reveals. |

> `CREATE` and `INSERT` are previewed here only to set up data to query — they
> are taught fully in a later session. Today's focus is the **querying**.

---

## 🎯 Skills you will practise across all three

- Retrieving data with `SELECT *` and specific-column selection
- **Filtering rows** with `WHERE` (text, numbers, and dates)
- Combining conditions with `AND`, and ranges with `BETWEEN`
- **Sorting** results with `ORDER BY … ASC / DESC`
- Combining all three into the workhorse pattern: **SELECT → FROM → WHERE → ORDER BY**
- Reading a business **insight** out of a query result

---

## 💡 The pattern to notice

Every real business question maps onto the same shape:

```sql
SELECT  (the columns to show)
FROM    (the table)
WHERE   (which rows matter)
ORDER BY (how to rank them);
```

Master these three clauses and you can answer a huge range of analytical
questions directly from a database — exactly what a junior data analyst does
every day.

---

*Happy querying! Start with Case Study 1 (Customers) — it is the simplest and
introduces every clause you'll reuse in the other two.* 🚀
