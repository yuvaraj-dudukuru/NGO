# Case Study 2 — Customer Analytics

**Business context:** The marketing team needs customer segmentation and behavioural
analysis to design targeted campaigns. We build a per-customer value profile, compare
revenue across segments, and use a `LEFT JOIN` to find customers who have never ordered.

---

## Files

| File           | Purpose                                                        |
| -------------- | ------------------------------------------------------------- |
| `schema.sql`   | Creates the `Customers` and `Orders` tables.                   |
| `data.sql`     | Inserts the sample data (5 customers, 6 orders).               |
| `queries.sql`  | The three queries (23.1 value profile, 23.2 segment revenue, 23.3 inactive customers). |
| `run_all.sql`  | Runner that builds the schema, loads the data, and runs every query. |
| `README.md`    | This file.                                                    |

### Data model

```
Customers(CustomerID PK, CustomerName, Segment, City)
Orders   (OrderID    PK, CustomerID FK, ProductID, OrderAmount)
```

There are 5 registered customers: 2 Premium and 2 Regular are active, plus **Karan**
(Premium) who has never placed an order — he is the "inactive" customer found by 23.3.

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

`:memory:` keeps the database in RAM only, so results print to screen and nothing is
written to disk. For a persisted file use `sqlite3 customers.db ".read run_all.sql"`.

---

## How to stop

- The command runs once and **exits on its own** — there is no background process.
- In an interactive `sqlite3` shell, type `.quit` (or `Ctrl+D`) to exit; `Ctrl+C`
  interrupts a running statement.
- Delete any optional saved database file to clean up: `rm customers.db`.

---

## Expected output

**23.1 Customer Value Profile**

```
CustomerName  Segment  OrderCount  TotalSpent  AvgOrderValue
------------  -------  ----------  ----------  -------------
Rajesh        Premium  3           93600       31200.0
Aman          Premium  1           60000       60000.0
Priya         Regular  1           60000       60000.0
Sneha         Regular  1           30000       30000.0
```

> Priya and Aman both spent 60,000. With a tie on `TotalSpent` and no tie-breaker column
> in `ORDER BY`, their relative order is not guaranteed and may differ between engines.

**23.2 Revenue by Segment**

```
Segment  SegmentRevenue  Customers
-------  --------------  ---------
Premium  153600          2
Regular  90000           2
```

**23.3 Inactive Customers** (`LEFT JOIN` + `WHERE o.OrderID IS NULL`)

```
CustomerName  City
------------  ---------
Karan         Hyderabad
```

---

## Findings & recommendations

- **Premium** customers generate **₹1,53,600** vs **₹90,000** from **Regular** customers,
  despite equal headcount — the Premium segment is disproportionately valuable.
- **Rajesh** is the most frequent purchaser; **Priya** and **Aman** have the highest
  average order values.
- **Karan** is a registered Premium customer who has **never ordered** — a clear target
  for a re-engagement campaign.
- **Recommendations:** invest in retaining and growing the Premium segment; launch a
  re-engagement campaign for inactive customers like Karan; study why high-frequency and
  high-value behaviours differ across customers.

> All customer names here are **fictional sample data** used only to demonstrate the queries.
