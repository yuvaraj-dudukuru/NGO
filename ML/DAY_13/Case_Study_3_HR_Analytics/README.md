# Case Study 3 — HR Analytics

**Business context:** The HR department needs a departmental analysis of headcount,
compensation, and performance. A single `Employees` table is grouped and aggregated to
summarise each department, flag high performers, and measure salary spread.

---

## Files

| File           | Purpose                                                        |
| -------------- | ------------------------------------------------------------- |
| `schema.sql`   | Creates the `Employees` table.                                 |
| `data.sql`     | Inserts the sample data (5 employees across IT/HR/Finance).    |
| `queries.sql`  | The three queries (24.1 dept summary, 24.2 high performers, 24.3 salary range). |
| `run_all.sql`  | Runner that builds the schema, loads the data, and runs every query. |
| `README.md`    | This file.                                                    |

### Data model

```
Employees(EmpID PK, Name, Department, Salary, PerformanceScore)
```

| EmpID | Name  | Department | Salary  | PerformanceScore |
| ----- | ----- | ---------- | ------- | ---------------- |
| 1     | Asha  | IT         | 90000   | 88               |
| 2     | Ravi  | HR         | 55000   | 72               |
| 3     | Imran | IT         | 120000  | 95               |
| 4     | Divya | Finance    | 60000   | 65               |
| 5     | Karan | IT         | 75000   | 80               |

---

## Prerequisites

You only need the **SQLite** command-line tool (`sqlite3`). Everything runs in-memory —
there is **no database server** to install, start, or stop.

- Check it is installed: `sqlite3 --version`
- If missing, install it:
  - Windows: `winget install SQLite.SQLite` (or download the tools from sqlite.org)
  - macOS: `brew install sqlite`
  - Debian/Ubuntu: `sudo apt-get install sqlite3`

---

## How to run

Open a terminal **in this folder** and run:

```sh
sqlite3 :memory: ".read run_all.sql"
```

`:memory:` keeps the database in RAM only. For a persisted file use
`sqlite3 hr.db ".read run_all.sql"`.

---

## How to stop

- The command runs once and **exits on its own** — there is no background process.
- In an interactive `sqlite3` shell, type `.quit` (or `Ctrl+D`); `Ctrl+C` interrupts a
  running statement.
- Delete any optional saved database file to clean up: `rm hr.db`.

---

## Expected output

**24.1 Department Summary** (`AVG(PerformanceScore)` rounded to 2 dp for display)

```
Department  Headcount  TotalSalary  AvgSalary  AvgPerformance
----------  ---------  -----------  ---------  --------------
IT          3          285000       95000.0    87.67
Finance     1          60000        60000.0    65.0
HR          1          55000        55000.0    72.0
```

**24.2 High-Performing Departments** (average score > 75)

```
Department  AvgPerformance
----------  --------------
IT          87.67
```

**24.3 Salary Range by Department**

```
Department  LowestSalary  HighestSalary  SalaryRange
----------  ------------  -------------  -----------
Finance     60000         60000          0
HR          55000         55000          0
IT          75000         120000         45000
```

> 24.3 has **no `ORDER BY`** (matching the source case study), so the row order is not
> guaranteed and may differ between engines. Add `ORDER BY SalaryRange DESC` if you want
> a fixed order.

---

## Findings & recommendations

- **IT** is the largest department (3 employees) with the **highest average salary**
  (₹95,000) and the **highest average performance** (87.67), but also the **widest salary
  range** (₹45,000) — significant internal pay variation.
- Only **IT** meets the high-performance threshold (average score > 75).
- The wide IT salary range warrants a pay-equity review and a plan to retain top
  performers such as **Imran** (score 95, salary ₹1,20,000).
- **Recommendations:** review IT compensation for internal equity; document the practices
  behind IT's strong performance so they can be replicated in HR and Finance; keep high
  performers competitively compensated to reduce attrition risk.

> All employee names here are **fictional sample data** used only to demonstrate the queries.
