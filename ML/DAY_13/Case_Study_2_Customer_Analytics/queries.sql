-- ============================================================
-- Case Study 2: Customer Analytics
-- File: queries.sql  -- the analytical queries
-- ============================================================

-- ------------------------------------------------------------
-- 23.1 Customer Value Profile
-- Per-customer order count, total spend and average order value.
-- ------------------------------------------------------------
SELECT c.CustomerName,
       c.Segment,
       COUNT(o.OrderID)   AS OrderCount,
       SUM(o.OrderAmount) AS TotalSpent,
       AVG(o.OrderAmount) AS AvgOrderValue
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName, c.Segment
ORDER BY TotalSpent DESC;

-- ------------------------------------------------------------
-- 23.2 Revenue by Segment
-- Compare Premium vs Regular revenue and customer counts.
-- ------------------------------------------------------------
SELECT c.Segment,
       SUM(o.OrderAmount)           AS SegmentRevenue,
       COUNT(DISTINCT c.CustomerID) AS Customers
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.Segment;

-- ------------------------------------------------------------
-- 23.3 Inactive Customers
-- LEFT JOIN keeps every customer; WHERE o.OrderID IS NULL keeps
-- only those with no matching order (never purchased).
-- ------------------------------------------------------------
SELECT c.CustomerName, c.City
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;
