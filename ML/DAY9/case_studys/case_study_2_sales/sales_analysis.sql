-- ============================================================================
-- CASE STUDY 2 — SALES DATABASE ANALYSIS
-- ----------------------------------------------------------------------------
-- Business context:
--   A sales manager wants to review recent high-value orders. We use the
--   Orders table from the Day 9 notes (Section 7.2).
--
-- What you will practise here:
--   * Retrieving specific columns
--   * Filtering NUMERIC data with WHERE (Amount > ...)
--   * Filtering DATE data with BETWEEN (a date range)
--   * Sorting with ORDER BY ... DESC and ... ASC
--
-- How to run this file:
--   * SQLite CLI:  sqlite3 < sales_analysis.sql
--   * Python:      conn.executescript(open("sales_analysis.sql").read())
--   * Or paste the queries into any SQL tool.
-- ============================================================================


-- ============================================================================
-- SETUP — build the table to query
-- (CREATE / INSERT are previewed here only to set up data; taught fully later.)
-- ============================================================================
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    OrderID    INTEGER PRIMARY KEY,   -- unique label for each order
    CustomerID INTEGER,               -- foreign key -> customers.CustomerID
    Product    TEXT,
    Amount     INTEGER,
    OrderDate  TEXT                    -- stored as 'YYYY-MM-DD'
);

INSERT INTO orders VALUES (5001, 101, 'Laptop', 60000, '2026-06-01');
INSERT INTO orders VALUES (5002, 102, 'Phone',  30000, '2026-06-02');
INSERT INTO orders VALUES (5003, 101, 'Mouse',   1200, '2026-06-03');
INSERT INTO orders VALUES (5004, 103, 'Tablet', 20000, '2026-06-05');
INSERT INTO orders VALUES (5005, 104, 'Phone',  30000, '2026-06-07');


-- ============================================================================
-- 1. RETRIEVE ALL ORDERS
-- ============================================================================
-- List the columns we care about (better than SELECT * in a real report).
SELECT OrderID, Product, Amount, OrderDate
FROM orders;


-- ============================================================================
-- 2. FILTER — high-value orders only
-- ============================================================================
-- Numbers do NOT take quotes. ORDER BY DESC puts the biggest sale on top.
SELECT Product, Amount
FROM orders
WHERE Amount > 25000
ORDER BY Amount DESC;

-- Expected output:
--   Product | Amount
--   --------+-------
--   Laptop  | 60000
--   Phone   | 30000
--   Phone   | 30000
--
-- INSIGHT:
-- The Laptop is the single highest-value sale; Phones appear twice as strong
-- contributors.


-- ============================================================================
-- 3. FILTER BY DATE — this week's orders
-- ============================================================================
-- Dates use quotes like text, in 'YYYY-MM-DD' format. BETWEEN is inclusive of
-- both ends. ORDER BY OrderDate ASC lists them earliest-first.
SELECT OrderID, Product, Amount, OrderDate
FROM orders
WHERE OrderDate BETWEEN '2026-06-01' AND '2026-06-05'
ORDER BY OrderDate ASC;

-- Expected output:
--   OrderID | Product | Amount | OrderDate
--   --------+---------+--------+-----------
--   5001    | Laptop  | 60000  | 2026-06-01
--   5002    | Phone   | 30000  | 2026-06-02
--   5003    | Mouse   | 1200   | 2026-06-03
--   5004    | Tablet  | 20000  | 2026-06-05
--
-- INSIGHT & RECOMMENDATION:
-- Early-June orders are dominated by electronics, led by the Laptop. The manager
-- can confidently report that high-value electronics drive early-month revenue
-- and plan stock accordingly.
