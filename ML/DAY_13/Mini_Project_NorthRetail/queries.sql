-- ============================================================
-- Mini Project: NorthRetail
-- File: queries.sql  -- the analytical reports
-- ============================================================

-- ------------------------------------------------------------
-- 3. Master report: every order, fully described
--    (Orders INNER JOIN Customers INNER JOIN Products)
-- ------------------------------------------------------------
SELECT o.OrderID,
       c.CustomerName,
       c.City,
       p.ProductName,
       p.Category,
       o.Quantity,
       o.OrderAmount
FROM Orders o
INNER JOIN Customers c ON o.CustomerID = c.CustomerID
INNER JOIN Products  p ON o.ProductID  = p.ProductID
ORDER BY o.OrderID;

-- ------------------------------------------------------------
-- 4. Key Performance Indicators
-- ------------------------------------------------------------
SELECT COUNT(*)                   AS Orders,
       COUNT(DISTINCT CustomerID) AS Customers,
       SUM(OrderAmount)           AS Revenue,
       AVG(OrderAmount)           AS AvgOrderValue
FROM Orders;

-- ------------------------------------------------------------
-- 5a. Revenue by category, ranked descending
-- ------------------------------------------------------------
SELECT p.Category,
       SUM(o.OrderAmount) AS Revenue,
       COUNT(*)           AS Orders
FROM Orders o
INNER JOIN Products p ON o.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Revenue DESC;

-- ------------------------------------------------------------
-- 5b. High-value customers: total spend above 50,000 (HAVING)
-- ------------------------------------------------------------
SELECT c.CustomerName,
       c.City,
       COUNT(*)           AS Orders,
       SUM(o.OrderAmount) AS TotalSpent
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerID, c.CustomerName, c.City
HAVING SUM(o.OrderAmount) > 50000
ORDER BY TotalSpent DESC;

-- ------------------------------------------------------------
-- 5c. Orders and revenue by city
-- ------------------------------------------------------------
SELECT c.City,
       COUNT(*)           AS Orders,
       SUM(o.OrderAmount) AS Revenue
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.City
ORDER BY Revenue DESC;

-- ------------------------------------------------------------
-- 5d. Best-selling products by total quantity
-- ------------------------------------------------------------
SELECT p.ProductName,
       p.Category,
       SUM(o.Quantity)    AS UnitsSold,
       SUM(o.OrderAmount) AS Revenue
FROM Products p
INNER JOIN Orders o ON p.ProductID = o.ProductID
GROUP BY p.ProductID, p.ProductName, p.Category
ORDER BY UnitsSold DESC;
