# Hands-On Activity — SQLite through Python

This activity combines the Jupyter/Python environment with the SQL of Day 13. It runs the
**complete analytical SQL workflow** against an **in-memory SQLite** database driven from
Python, using **pandas** for tidy table output.

SQLite is built into Python (the `sqlite3` module), so there is **nothing to install for
the database** and **no server to start or stop**.

The 8 steps:

1. Connect to a database and create a cursor
2. Create the tables (define the relational schema)
3. Populate the tables (insert sample data)
4. Perform an `INNER JOIN`
5. Use aggregate functions (`COUNT`, `SUM`, `AVG`)
6. Apply `GROUP BY`
7. Apply `HAVING` (filter groups after aggregation)
8. Generate a complete business report and close the connection

---

## Files

| File                      | Purpose                                                       |
| ------------------------- | ------------------------------------------------------------ |
| `hands_on_activity.py`    | The whole activity as a single runnable Python script.        |
| `hands_on_activity.ipynb` | The same workflow as a Jupyter notebook (one cell per step).  |
| `requirements.txt`        | Python dependencies (`pandas`; `sqlite3` is built-in).        |
| `README.md`               | This file.                                                   |

---

## Prerequisites

- **Python 3.8+** — check with `python --version`
- **pandas** — install with:

  ```sh
  python -m pip install -r requirements.txt
  ```

- *(Notebook only)* **Jupyter** — install with `python -m pip install jupyter`

> `sqlite3` is part of the Python standard library — no separate database install needed.

---

## How to run

### Option A — Python script (simplest)

From inside this folder:

```sh
python hands_on_activity.py
```

It prints the result of every step and ends with `Connection closed.`

### Option B — Jupyter notebook

```sh
python -m jupyter notebook hands_on_activity.ipynb
```

(or open the file in VS Code / JupyterLab) and run the cells top to bottom with
**Shift+Enter**.

To run the notebook headlessly without opening it:

```sh
python -m jupyter nbconvert --to notebook --execute hands_on_activity.ipynb
```

---

## How to stop

- The **script** runs once and exits on its own — there is no background process. Press
  `Ctrl+C` to abort early if needed.
- The database is in-memory and is released automatically by `conn.close()` (Step 8), so
  there is nothing to clean up on disk.
- For the **notebook server**: stop it with `Ctrl+C` in the terminal where it is running,
  or use *File → Shut Down* in the Jupyter UI. To release the kernel only, use
  *Kernel → Shut Down Kernel*.

---

## Expected output

```
Database connection established.

Tables created.

Sample data inserted.

Step 4 - INNER JOIN (customer name + each order amount):
  CustomerName  OrderAmount
0       Rajesh        60000
1        Priya        60000
2       Rajesh         3600
3         Aman        60000
4        Sneha        30000
5       Rajesh        30000

Step 5 - Aggregates over all orders:
   Orders  Revenue  AvgValue
0       6   243600   40600.0

Step 6 - Total spend per customer (GROUP BY):
   CustomerID  TotalSpent
0         101       93600
1         102       60000
2         103       60000
3         104       30000

Step 7 - Customers who spent more than 50,000 (HAVING):
   CustomerID  TotalSpent
0         101       93600
1         102       60000
2         103       60000

Step 8 - Business report (high-value customers):
  CustomerName       City  TotalSpent
0       Rajesh  Hyderabad       93600
1        Priya  Bengaluru       60000
2         Aman     Mumbai       60000

Connection closed.
```

> **Tie ordering note.** Customers 102 (Priya) and 103 (Aman) each total **60,000**.
> When two rows tie and the `ORDER BY` has no tie-breaker column, SQLite does not
> guarantee their relative order, so Steps 6 and 8 may show those two rows swapped on your
> machine. The values are identical either way. Add a tie-breaker (e.g.
> `ORDER BY TotalSpent DESC, CustomerID`) if you need a fixed order.

---

## What you practised

Creating a relational schema, populating it, performing joins and aggregations, applying
group-level filtering with `HAVING`, and producing a business report — the complete
analytical SQL workflow, all from Python.

> All names and figures are **fictional sample data** used only to demonstrate the workflow.
