-- ============================================================================
-- MINI CHALLENGE — "ShopNed" ONLINE STORE: EXPLORE THE ORDERS DATABASE
-- ----------------------------------------------------------------------------
-- Scenario: You are a junior data analyst at "ShopNed", an online store.
--           Management gives you the orders database and asks you to explore it,
--           run several analytical queries, and present business insights using
--           ONLY SELECT, WHERE, and ORDER BY.
--
-- What you will practise here:
--   * Exploring a table with SELECT * and specific-column selection
--   * Filtering numbers, text, AND-conditions, and OR-conditions
--   * Sorting with ORDER BY ... DESC
--   * Combining SELECT + WHERE + ORDER BY into one query
--   * Stretch goals: BETWEEN (dates), LIKE (names), multi-column sort
--
-- How to run this file:
--   * SQLite CLI:  sqlite3 < shopned_analysis.sql
--   * Python:      conn.executescript(open("shopned_analysis.sql").read())
--   * Or paste the queries into any SQL tool.
-- ============================================================================


-- ============================================================================
-- SETUP — create the database (simulates connecting to a real one)
-- (CREATE / INSERT are previewed here only to set up data; taught fully later.)
-- ============================================================================
DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    OrderID   INTEGER PRIMARY KEY,
    Customer  TEXT,
    City      TEXT,
    Product   TEXT,
    Amount    INTEGER,
    OrderDate TEXT                    -- stored as 'YYYY-MM-DD'
);

INSERT INTO orders VALUES (1, 'Asha',  'Pune',   'Laptop', 65000, '2026-05-02');
INSERT INTO orders VALUES (2, 'Ravi',  'Mumbai', 'Phone',  30000, '2026-05-03');
INSERT INTO orders VALUES (3, 'Imran', 'Pune',   'Mouse',   1200, '2026-05-05');
INSERT INTO orders VALUES (4, 'Divya', 'Delhi',  'Laptop', 60000, '2026-05-06');
INSERT INTO orders VALUES (5, 'Karan', 'Mumbai', 'Tablet', 20000, '2026-05-08');
INSERT INTO orders VALUES (6, 'Meena', 'Delhi',  'Phone',  30000, '2026-05-09');
INSERT INTO orders VALUES (7, 'Sahil', 'Pune',   'Laptop', 70000, '2026-05-11');
INSERT INTO orders VALUES (8, 'Tara',  'Mumbai', 'Watch',   8000, '2026-05-12');


-- ============================================================================
-- 1. EXPLORE THE TABLE — retrieve all records
-- ============================================================================
SELECT * FROM orders;
-- INSIGHT: 8 orders across 3 cities (Pune, Mumbai, Delhi).


-- ============================================================================
-- 2. RETRIEVE SPECIFIC DATA — Customer, Product, Amount
-- ============================================================================
SELECT Customer, Product, Amount
FROM orders;


-- ============================================================================
-- 3. APPLY FILTERS
-- ============================================================================

-- 3a. All orders above 25,000 (numbers need no quotes)
SELECT * FROM orders
WHERE Amount > 25000;

-- 3b. All orders from 'Pune' (text needs single quotes)
SELECT * FROM orders
WHERE City = 'Pune';

-- 3c. All Laptop orders in Pune above 50,000 (combine conditions with AND)
SELECT * FROM orders
WHERE City = 'Pune' AND Product = 'Laptop' AND Amount > 50000;

-- 3d. All orders from Mumbai OR Delhi (either condition qualifies)
SELECT * FROM orders
WHERE City = 'Mumbai' OR City = 'Delhi';


-- ============================================================================
-- 4. SORT RESULTS — all orders by Amount, highest first
-- ============================================================================
SELECT * FROM orders
ORDER BY Amount DESC;
-- INSIGHT: The highest-value order is Sahil's Laptop (70,000) in Pune;
-- Laptops dominate the top orders.


-- ============================================================================
-- 5. COMBINE SELECT + WHERE + ORDER BY
--    Customer, Product, Amount for orders above 20,000, biggest first
-- ============================================================================
SELECT Customer, Product, Amount
FROM orders
WHERE Amount > 20000
ORDER BY Amount DESC;
-- Expected output:
--   Customer | Product | Amount
--   ---------+---------+-------
--   Sahil    | Laptop  | 70000
--   Asha     | Laptop  | 65000
--   Divya    | Laptop  | 60000
--   Ravi     | Phone   | 30000
--   Meena    | Phone   | 30000


-- ============================================================================
-- 6. BUSINESS INSIGHTS + RECOMMENDATIONS  (see README for the full report)
-- ============================================================================
-- Insight 1: The highest-value order is Sahil's Laptop (70,000) in Pune, and
--            all three Laptop orders sit at the top — Laptops are the key
--            revenue driver.
--   -> Recommendation: Focus laptop promotions and premium-electronics stock.
--
-- Insight 2: Pune produces several high-value laptop sales (Asha 65k, Sahil 70k).
--   -> Recommendation: Treat Pune as a strong market for premium electronics.
--
-- Insight 3: Filtering above 25,000 returns mostly Laptops and Phones.
--   -> Recommendation: Keep high-value electronics well stocked; target Mumbai
--      and Delhi (several mid-value orders) for growth campaigns.


-- ============================================================================
-- STRETCH GOALS (optional)
-- ============================================================================

-- Stretch 1: Orders placed between two dates (BETWEEN is inclusive)
SELECT * FROM orders
WHERE OrderDate BETWEEN '2026-05-05' AND '2026-05-10'
ORDER BY OrderDate ASC;

-- Stretch 2: Customers whose names start with a chosen letter ('A' here).
--            % matches any characters after the 'A'.
SELECT * FROM orders
WHERE Customer LIKE 'A%';

-- Stretch 3: Sort by City ascending, then Amount descending (tie-breaker).
SELECT Customer, City, Product, Amount
FROM orders
ORDER BY City ASC, Amount DESC;

-- Stretch 4: To chart amount by product, load a query result into Pandas and
--            draw a Seaborn bar chart (combining Days 8 and 9). In Python:
--   import pandas as pd, seaborn as sns, matplotlib.pyplot as plt
--   df = pd.read_sql("SELECT Product, Amount FROM orders", conn)
--   sns.barplot(data=df, x="Product", y="Amount")   # bar height = avg amount
--   plt.title("Average Amount by Product"); plt.show()
