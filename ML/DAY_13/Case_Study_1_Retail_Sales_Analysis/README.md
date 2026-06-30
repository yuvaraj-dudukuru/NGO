# Case Study 1 — Retail Sales Analysis

**Business context:** A retail company needs a sales analysis to guide inventory and
marketing decisions. We use JOINs, aggregations, `GROUP BY`, and `HAVING` to compute
headline KPIs, revenue by product category, and top customers.

---

## Files

| File           | Purpose                                                        |
| -------------- | ------------------------------------------------------------- |
| `schema.sql`   | Creates the `Customers`, `Products`, and `Orders` tables.      |
| `data.sql`     | Inserts the sample data (5 customers, 3 products, 6 orders).   |
| `queries.sql`  | The three analytical queries (22.1 KPIs, 22.2 category, 22.3 top customers). |
| `run_all.sql`  | Runner that builds the schema, loads the data, and runs every query. |
| `README.md`    | This file.                                                    |

### Data model

```
Customers(CustomerID PK, CustomerName, Segment, City)
Products (ProductID  PK, ProductName, Category)
Orders   (OrderID    PK, CustomerID FK, ProductID FK, OrderAmount)
```

The sample contains 5 registered customers but only **4 of them have ever ordered**
(Karan has none), which is why `COUNT(DISTINCT CustomerID)` over `Orders` returns 4.

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

Open a terminal **in this folder** (the runner uses relative paths) and run:

```sh
sqlite3 :memory: ".read run_all.sql"
```

`:memory:` means the database lives only in RAM for the duration of the command, so the
results print to your screen and **nothing is written to disk**.

Want a saved database file instead? Replace `:memory:` with a filename:

```sh
sqlite3 retail.db ".read run_all.sql"
```

You can also run the parts individually:

```sh
sqlite3 :memory: ".read schema.sql" ".read data.sql" ".read queries.sql"
```

---

## How to stop

- The command above runs once and **exits on its own** — there is no background process.
- If you open an **interactive** SQLite shell (`sqlite3`), leave it by typing `.quit`
  (or press `Ctrl+D`). To interrupt a long-running statement, press `Ctrl+C`.
- To clean up the optional saved database, just delete the file: `rm retail.db`.

---

## Expected output

**22.1 Key Performance Indicators**

```
TotalOrders  UniqueCustomers  TotalRevenue  AvgOrderValue
-----------  ---------------  ------------  -------------
6            4                243600        40600.0
```

**22.2 Revenue by Category**

```
Category     Revenue  Orders
-----------  -------  ------
Electronics  240000   5
Accessories  3600     1
```

**22.3 Top Customers** (total spend > 50,000)

```
CustomerName  TotalSpent
------------  ----------
Rajesh        93600
Priya         60000
Aman          60000
```

---

## Findings & recommendations

- Total revenue is **₹2,43,600** across **6 orders** from **4 unique customers**, an
  average order value of **₹40,600**.
- **Electronics generates ~98.5%** of revenue (₹2,40,000) — this is overwhelmingly an
  electronics retailer.
- **Rajesh** is the top customer at **₹93,600**, having placed 3 of the 6 orders.
- **Recommendations:** prioritise Electronics inventory and supplier relationships; build
  a loyalty programme for high-value customers like Rajesh; decide whether Accessories
  should be grown or treated as an add-on attached to Electronics sales.

> The customer/product names here are **fictional sample data** used only to demonstrate
> the queries.
