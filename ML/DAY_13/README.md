# Day 13 — Advanced SQL: JOINs, GROUP BY & HAVING

A complete, self-contained set of exercises for analytical SQL: three case studies, a
Python hands-on activity, and an end-to-end mini project. Every item lives in its **own
folder** with its schema, sample data, queries, a one-command runner, and a detailed README.

Everything targets **SQLite**, which needs **no database server** to install, start, or
stop — examples run in memory and print their results. Two of the items also drive that same
in-memory SQLite from **Python + pandas**.

---

## What's inside

| Folder | Type | Topic | Run with |
| ------ | ---- | ----- | -------- |
| [`Case_Study_1_Retail_Sales_Analysis/`](./Case_Study_1_Retail_Sales_Analysis) | Pure SQL | Sales KPIs, revenue by category, top customers | `sqlite3` |
| [`Case_Study_2_Customer_Analytics/`](./Case_Study_2_Customer_Analytics) | Pure SQL | Customer value profile, segment revenue, inactive customers | `sqlite3` |
| [`Case_Study_3_HR_Analytics/`](./Case_Study_3_HR_Analytics) | Pure SQL | Department summary, high performers, salary range | `sqlite3` |
| [`Hands_On_Activity_SQLite_with_Python/`](./Hands_On_Activity_SQLite_with_Python) | Python | The full 8-step analytical workflow | `python` (script **or** Jupyter notebook) |
| [`Mini_Project_NorthRetail/`](./Mini_Project_NorthRetail) | SQL **and** Python | Design → load → report → findings for a fictional retailer | `sqlite3` **or** `python` |

**SQL features covered across the set:** `INNER JOIN`, `LEFT JOIN` + `IS NULL`,
`GROUP BY`, `HAVING`, `COUNT`/`SUM`/`AVG`/`MIN`/`MAX`, `COUNT(DISTINCT ...)`, `ROUND`,
primary keys and foreign keys.

---

## Directory layout

```
DAY_13/
├── README.md                         <- you are here
│
├── Case_Study_1_Retail_Sales_Analysis/   ┐
├── Case_Study_2_Customer_Analytics/      ├ each: schema.sql, data.sql, queries.sql,
├── Case_Study_3_HR_Analytics/            ┘        run_all.sql, README.md
│
├── Hands_On_Activity_SQLite_with_Python/
│   ├── hands_on_activity.py          <- script version
│   ├── hands_on_activity.ipynb       <- Jupyter notebook version
│   ├── requirements.txt
│   └── README.md
│
└── Mini_Project_NorthRetail/
    ├── mini_project.py               <- Python version (incl. written findings)
    ├── schema.sql, data.sql, queries.sql, run_all.sql   <- pure-SQL version
    ├── requirements.txt
    └── README.md
```

In every folder: `schema.sql` defines tables, `data.sql` inserts sample rows,
`queries.sql` holds the analytical queries, and `run_all.sql` runs all three in one go.

---

## Prerequisites

**For the SQL items** — the SQLite command-line tool:

```sh
sqlite3 --version
```

If it is missing:
- **Windows:** `winget install SQLite.SQLite` (or download "sqlite-tools" from sqlite.org)
- **macOS:** `brew install sqlite`
- **Debian/Ubuntu:** `sudo apt-get install sqlite3`

**For the Python items** (hands-on activity and the mini project's Python version) —
Python 3.8+ and pandas. `sqlite3` is built into Python, so only pandas needs installing:

```sh
python -m pip install pandas        # or: python -m pip install -r requirements.txt
```

The Jupyter notebook additionally needs `python -m pip install jupyter`.

---

## How to run

**SQL case studies & the mini project's SQL version** — open a terminal **inside the
folder** (the runners use relative paths) and run:

```sh
sqlite3 :memory: ".read run_all.sql"
```

`:memory:` runs everything in RAM and writes nothing to disk. To keep a database file,
use a name instead: `sqlite3 mydb.db ".read run_all.sql"`.

**Python hands-on activity** (inside `Hands_On_Activity_SQLite_with_Python/`):

```sh
python hands_on_activity.py
# notebook instead:  python -m jupyter notebook hands_on_activity.ipynb
```

**Mini project** (inside `Mini_Project_NorthRetail/`) — either path works:

```sh
python mini_project.py                  # Python + pandas, includes findings
sqlite3 :memory: ".read run_all.sql"    # pure SQLite
```

> **Windows note:** these commands work as written in PowerShell and `cmd`. Do **not** use
> the Unix `< file.sql` redirection in PowerShell — it is unsupported there; use the
> `".read ..."` form shown above.

---

## How to stop

- Every command runs **once and exits on its own** — there is no server or background
  process to shut down. Press `Ctrl+C` to abort early.
- In-memory databases are released automatically (the Python scripts call `conn.close()`),
  so nothing is left on disk. Delete any named `.db` file you created to clean up.
- For an interactive SQLite shell (`sqlite3` with no script), exit with `.quit` or `Ctrl+D`.
- For a running Jupyter server, stop it with `Ctrl+C` in its terminal, or *File → Shut Down*.

---


## Notes

- **No personal data.** All names, cities, and figures are **fictional sample data** chosen
  only to demonstrate the SQL — no real, private, or personal information is included, and
  no machine-specific paths are embedded (all commands are relative).
- **Portability.** The SQL is standard and ports to MySQL/PostgreSQL with minor tweaks. The
  `.read`, `.mode`, and `.headers` commands are SQLite shell ("dot") commands, not SQL
  itself; the queries inside `queries.sql` are portable.
- **Reproducible results.** Where a report has tied values and no tie-breaker column in
  `ORDER BY`, the order of the tied rows is not guaranteed and may differ between engines;
  the affected folders note this and show how to force a fixed order.
