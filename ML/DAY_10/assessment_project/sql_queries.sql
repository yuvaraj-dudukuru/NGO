-- ============================================================================
-- FreshBasket — SQL Analysis (Day 9)
-- Table: sales  (the cleaned dataset, loaded via df.to_sql("sales", conn))
-- Each query is labelled with the BUSINESS QUESTION it answers.
-- ============================================================================

-- Q1. BUSINESS QUESTION: "Which category brings the most revenue?"
--     Technique: GROUP BY + SUM + ORDER BY
SELECT Category, SUM(Amount) AS TotalRevenue
FROM sales
GROUP BY Category
ORDER BY TotalRevenue DESC;
-- Result: Electronics 135000 | Grocery 9100 | Clothing 5700


-- Q2. BUSINESS QUESTION: "Which city brings the most revenue?"
SELECT City, SUM(Amount) AS Revenue
FROM sales
GROUP BY City
ORDER BY Revenue DESC;
-- Result: Pune 135000 | Mumbai 8400 | Delhi 6400
-- NOTE: Pune leads REVENUE even though Mumbai has more ORDERS (see Q below).


-- Q3. BUSINESS QUESTION: "Which orders are high-value (above Rs.10,000)?"
--     Technique: WHERE + ORDER BY
SELECT Customer, Category, Amount
FROM sales
WHERE Amount > 10000
ORDER BY Amount DESC;
-- Result: Sahil/Electronics/52000, Ravi/Electronics/45000, Imran/Electronics/38000


-- Q4. BUSINESS QUESTION: "Who are our customers in Pune?"
--     Technique: WHERE filter
SELECT Customer, Amount
FROM sales
WHERE City = 'Pune';
-- Result: Ravi 45000, Imran 38000, Sahil 52000  (all high-value Electronics buyers)


-- ---------------------------------------------------------------------------
-- SUPPORTING QUERY (order frequency vs revenue, explains the Pune/Mumbai split)
-- BUSINESS QUESTION: "Which city has the most orders?"
SELECT City, COUNT(*) AS Orders
FROM sales
GROUP BY City
ORDER BY Orders DESC;
-- Result: Mumbai 4 | Pune 3 | Delhi 2
