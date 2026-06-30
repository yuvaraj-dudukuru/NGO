# Mini Project — NorthRetail Analytical SQL

**Role:** data analyst at **NorthRetail**, a multi-category retail company.

**Goal:** design a small relational database, populate it with sample data, and produce a
set of analytical business reports using `JOIN`, `GROUP BY`, and `HAVING` — moving from raw
tables to business insight.

The project is provided **two ways** so you can run it however you like:

- **Python + pandas** (`mini_project.py`) — matches the suggested solution structure and
  prints a documented findings summary.
- **Pure SQLite** (`schema.sql` / `data.sql` / `queries.sql` / `run_all.sql`) — no Python
  needed.

Both produce identical numbers.

---

## Files

| File             | Purpose                                                          |
| ---------------- | --------------------------------------------------------------- |
| `mini_project.py`| Full solution in Python: build, load, all reports, findings.     |
| `schema.sql`     | `CREATE TABLE` for `Customers`, `Products`, `Orders` (PKs + FKs). |
| `data.sql`       | Sample data: 8 customers, 5 products, 15 orders.                  |
| `queries.sql`    | The six analytical reports (master, KPIs, 4 reports).            |
| `run_all.sql`    | Pure-SQLite runner (schema + data + queries).                    |
| `requirements.txt`| Python dependency (`pandas`; `sqlite3` is built-in).            |
| `README.md`      | This file.                                                       |

### Data model

```
Customers(CustomerID PK, CustomerName, City)
Products (ProductID  PK, ProductName, Category, Price)
Orders   (OrderID    PK, CustomerID FK -> Customers,
                         ProductID  FK -> Products,
                         Quantity, OrderAmount, OrderDate)
```

- **8 customers** across 4 cities (Hyderabad, Bengaluru, Mumbai, Delhi).
- **5 products** across 3 categories (Electronics, Accessories, Furniture).
- **15 orders**, with `OrderAmount = Quantity * Price`.

---

## Requirements covered

1. **Design tables** — `Customers`, `Products`, `Orders` with primary keys and foreign keys
   linking orders to customers and products.
2. **Load sample data** — 8 customers, 5 products (3 categories), 15 orders.
3. **Joins** — a master report joining all three tables.
4. **KPIs** — total revenue, total orders, unique customers, average order value.
5. **Reports** — revenue by category (ranked); high-value customers (`HAVING`); orders &
   revenue by city; best-selling products by quantity.
6. **Findings** — top category, top customers, strongest city, and recommendations.

---

## Prerequisites

**For the pure-SQLite path:** the `sqlite3` command-line tool (`sqlite3 --version`).

**For the Python path:** Python 3.8+ and pandas:

```sh
python -m pip install -r requirements.txt
```

> `sqlite3` is built into Python and into the standalone CLI — there is **no database
> server** to install, start, or stop.

---

## How to run

### Option A — Python (recommended; includes the written findings)

From inside this folder:

```sh
python mini_project.py
```

### Option B — Pure SQLite

```sh
sqlite3 :memory: ".read run_all.sql"
```

`:memory:` runs everything in RAM and writes nothing to disk. Use a filename
(`sqlite3 northretail.db ".read run_all.sql"`) if you want a saved database.

---

## How to stop

- Both commands run **once and exit on their own** — there is no server or background
  process. Press `Ctrl+C` to abort early.
- The Python script closes its in-memory connection at the end (`conn.close()`), so nothing
  is left behind. For the SQLite path, in-memory runs leave no file; delete any named `.db`
  you created to clean up.

---

## Expected output (key figures)

**KPIs**

```
Orders  Customers  Revenue  AvgOrderValue
15      8          510000   34000.0
```

**5a. Revenue by category (ranked)**

```
Category     Revenue  Orders
Electronics  450000   9
Furniture    48000    4
Accessories  12000    2
```

**5b. High-value customers (spend > 50,000)**

```
CustomerName  City       Orders  TotalSpent
Rajesh        Hyderabad  3       96000
Karan         Hyderabad  2       76000
Meera         Bengaluru  2       72000
Vikram        Mumbai     2       72000
Aman          Mumbai     2       68000
Priya         Bengaluru  2       66000
```

**5c. Orders & revenue by city**

```
City       Orders  Revenue
Hyderabad  5       172000
Mumbai     4       140000
Bengaluru  4       138000
Delhi      2       60000
```

**5d. Best-selling products (by units sold)**

```
ProductName   Category     UnitsSold  Revenue
Phone         Electronics  7          210000
Headphones    Accessories  6          12000
Laptop        Electronics  4          240000
Office Chair  Furniture    3          24000
Desk          Furniture    2          24000
```

> Where a report has tied values and no tie-breaker column in `ORDER BY` (e.g. Meera and
> Vikram both at 72,000), the relative order of the tied rows is not guaranteed and may
> differ between engines.

---

## Findings & recommendations

- **Total business:** ₹5,10,000 revenue across **15 orders** from **8 customers**, an
  average order value of **₹34,000**.
- **Top category:** **Electronics** at ₹4,50,000 — **~88%** of all revenue. The business is
  overwhelmingly electronics-led.
- **Strongest city:** **Hyderabad** at ₹1,72,000 across 5 orders, ahead of Mumbai
  (₹1,40,000) and Bengaluru (₹1,38,000). **Delhi** is the weakest at ₹60,000 (2 orders).
- **Top customers:** **Rajesh** (₹96,000) leads, followed by Karan (₹76,000), Meera and
  Vikram (₹72,000 each). **6 of 8** customers spend above the ₹50,000 threshold.
- **Volume vs. value:** **Phone** sells the most units (7), but **Laptop** earns the most
  revenue (₹2,40,000). Headphones move in volume (6 units) yet contribute little revenue
  (₹12,000).

**Recommendations**

1. **Prioritise Electronics** inventory and supplier relationships — it drives ~88% of
   revenue; protect availability of Laptops and Phones.
2. **Reward high-value customers** (Rajesh, Karan, Meera, Vikram, Aman, Priya) with a
   loyalty programme or targeted offers to defend the bulk of revenue.
3. **Grow the strongest market (Hyderabad)** while running a **re-engagement / local
   promotion campaign in Delhi**, which is clearly underperforming.
4. **Use volume to lift value:** bundle Accessories (Headphones) with high-volume Phones and
   upsell Laptops to Phone buyers, so the small Accessories and Furniture categories grow
   on the back of Electronics traffic.

> All names and figures are **fictional sample data** used only to demonstrate the analysis.
