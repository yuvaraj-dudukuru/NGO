# Day 9 — SQL for Data Analysis

Day 9 answers business questions **directly from a database** using the three
core SQL commands: **`SELECT`**, **`WHERE`**, and **`ORDER BY`** (plus
`GROUP BY` / `SUM` / `COUNT` for aggregation). These are the SQL equivalents of
the Pandas analyses from Day 8.

Everything runs on **SQLite**, which is built into Python — no database server to
install.

---

## What's in this folder

| Item | Type | What it is |
|------|------|-----------|
| [`case_studys/`](case_studys/) | folder | **Three case studies** (customers, sales, employees), each a self-contained `.sql` file + README |
| [`mini_challenge/`](mini_challenge/) | folder | **ShopNed** — explore an orders database with several analytical queries |

### Case studies

| # | Folder | Table | Question |
|---|--------|-------|----------|
| 1 | [`case_study_1_customers/`](case_studys/case_study_1_customers/) | customers | Who are the top customers, and where? |
| 2 | [`case_study_2_sales/`](case_studys/case_study_2_sales/) | orders | Which products and dates drive sales? |
| 3 | [`case_study_3_employees/`](case_studys/case_study_3_employees/) | employees | Pay and department comparisons |

> Each `.sql` file is **fully self-contained**: it `CREATE`s its table,
> `INSERT`s sample rows, and then runs the analysis queries. All data is
> synthetic — no real personal data.

---

## How to Run

**Option A — SQLite command line** (if you have the `sqlite3` CLI):

```bash
cd case_studys/case_study_1_customers
sqlite3 < customers_analysis.sql
```

**Option B — from Python** (always available, no extra install):

```bash
python -c "import sqlite3; sqlite3.connect(':memory:').executescript(open('customers_analysis.sql').read())"
```

**Option C — a database GUI** (DB Browser for SQLite, etc.): open the `.sql`
file and click *Execute*.

Each script creates its table, loads the rows, and returns the query results.

---

## How to Stop

SQL scripts run once and finish immediately — there is nothing to stop. If you
opened an interactive `sqlite3` shell, type `.quit` (or press **`Ctrl + C`**) to
exit it.

---

## Requirements

**None to install** — `sqlite3` ships with Python's standard library. The
optional `sqlite3` command-line tool and GUI browsers are conveniences, not
requirements.
