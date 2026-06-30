-- ============================================================
-- Case Study 1: Retail Sales Analysis
-- File: queries.sql  -- the analytical queries
-- ============================================================

-- ------------------------------------------------------------
-- 22.1 Key Performance Indicators
-- Headline sales KPIs in a single pass over Orders.
-- COUNT(DISTINCT CustomerID) separates *customers* from *orders*.
-- ------------------------------------------------------------
SELECT COUNT(*)                   AS TotalOrders,
       COUNT(DISTINCT CustomerID) AS UniqueCustomers,
       SUM(OrderAmount)           AS TotalRevenue,
       AVG(OrderAmount)           AS AvgOrderValue
FROM Orders;

-- ------------------------------------------------------------
-- 22.2 Revenue by Category
-- Join orders to products, then aggregate per category.
-- ------------------------------------------------------------
SELECT p.Category,
       SUM(o.OrderAmount) AS Revenue,
       COUNT(*)           AS Orders
FROM Orders o
INNER JOIN Products p ON o.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Revenue DESC;

-- ------------------------------------------------------------
-- 22.3 Top Customers
-- HAVING filters *after* aggregation: keep customers whose
-- total spend exceeds 50,000.
-- ------------------------------------------------------------
SELECT c.CustomerName,
       SUM(o.OrderAmount) AS TotalSpent
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName
HAVING SUM(o.OrderAmount) > 50000
ORDER BY TotalSpent DESC;
