-- ============================================================================
-- CASE STUDY 1 — CUSTOMER DATABASE ANALYSIS
-- ----------------------------------------------------------------------------
-- Business context:
--   A retail company wants to understand its customer base for a marketing
--   campaign. We use the Customers table from the Day 9 notes (Section 7.1).
--
-- What you will practise here:
--   * Retrieving a whole table with SELECT *
--   * Filtering rows with WHERE on a TEXT column
--   * Sorting results with ORDER BY ... DESC
--   * Combining WHERE + ORDER BY into one analytical query
--
-- How to run this file:
--   * SQLite CLI:  sqlite3 < customers_analysis.sql
--   * Python:      conn.executescript(open("customers_analysis.sql").read())
--   * Or paste the queries into any SQL tool.
-- ============================================================================


-- ============================================================================
-- SETUP — build the table to query
-- (CREATE / INSERT are previewed here only to set up data; taught fully later.)
-- ============================================================================
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    CustomerID INTEGER PRIMARY KEY,   -- unique label for each customer
    Name       TEXT,
    City       TEXT,
    Age        INTEGER
);

INSERT INTO customers VALUES (101, 'Rajesh', 'Hyderabad', 28);
INSERT INTO customers VALUES (102, 'Priya',  'Bengaluru', 34);
INSERT INTO customers VALUES (103, 'Aman',   'Mumbai',    22);
INSERT INTO customers VALUES (104, 'Sneha',  'Delhi',     41);
INSERT INTO customers VALUES (105, 'Karan',  'Hyderabad', 30);


-- ============================================================================
-- 1. DATA RETRIEVAL — see the whole table
-- ============================================================================
-- SELECT * returns every column, like df.head() in Pandas. A quick first look.
SELECT * FROM customers;

-- INSIGHT:
-- We have 5 customers across 4 cities (Hyderabad appears twice).


-- ============================================================================
-- 2. FILTERING — target a specific city
-- ============================================================================
-- WHERE keeps only rows where the condition is true. Text values need single
-- quotes ('Hyderabad').
SELECT Name, Age
FROM customers
WHERE City = 'Hyderabad';

-- INSIGHT:
-- Two customers (Rajesh, Karan) are in Hyderabad — a target group for a local
-- campaign.


-- ============================================================================
-- 3. SORTING — rank by age
-- ============================================================================
-- ORDER BY ... DESC sorts from largest to smallest (oldest first here).
SELECT Name, City, Age
FROM customers
ORDER BY Age DESC;

-- INSIGHT:
-- The oldest customer is Sneha (41); the youngest is Aman (22). Knowing the age
-- spread helps tailor the campaign's messaging.


-- ============================================================================
-- 4. COMBINED ANALYSIS — older customers, sorted
-- ============================================================================
-- The workhorse pattern: SELECT (columns) -> FROM (table) -> WHERE (rows)
-- -> ORDER BY (sort). Keep customers aged 30+ and rank them oldest first.
SELECT Name, City, Age
FROM customers
WHERE Age >= 30
ORDER BY Age DESC;

-- Expected output:
--   Name  | City      | Age
--   ------+-----------+----
--   Sneha | Delhi     | 41
--   Priya | Bengaluru | 34
--   Karan | Hyderabad | 30
--
-- INSIGHT & RECOMMENDATION:
-- Three customers are 30 or older. For a premium product aimed at mature
-- customers, this filtered, ranked list is exactly the target audience — a
-- complete mini-analysis from one query.
