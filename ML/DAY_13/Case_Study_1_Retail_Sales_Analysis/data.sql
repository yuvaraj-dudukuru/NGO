-- ============================================================
-- Case Study 1: Retail Sales Analysis
-- File: data.sql  -- sample data
-- ============================================================

-- 5 registered customers. Karan has never placed an order
-- (so the analytics see only 4 *active* customers).
INSERT INTO Customers (CustomerID, CustomerName, Segment, City) VALUES
(1, 'Rajesh', 'Premium', 'Mumbai'),
(2, 'Priya',  'Regular', 'Delhi'),
(3, 'Aman',   'Premium', 'Bengaluru'),
(4, 'Sneha',  'Regular', 'Pune'),
(5, 'Karan',  'Premium', 'Hyderabad');

-- 3 products: two Electronics, one Accessories.
INSERT INTO Products (ProductID, ProductName, Category) VALUES
(1, 'Laptop',     'Electronics'),
(2, 'Smartphone', 'Electronics'),
(3, 'Mouse',      'Accessories');

-- 6 orders from 4 customers (Karan has none).
INSERT INTO Orders (OrderID, CustomerID, ProductID, OrderAmount) VALUES
(1, 1, 1, 45000),   -- Rajesh, Laptop      (Electronics)
(2, 1, 2, 45000),   -- Rajesh, Smartphone  (Electronics)
(3, 1, 3,  3600),   -- Rajesh, Mouse       (Accessories)
(4, 2, 1, 60000),   -- Priya,  Laptop      (Electronics)
(5, 3, 2, 60000),   -- Aman,   Smartphone  (Electronics)
(6, 4, 1, 30000);   -- Sneha,  Laptop      (Electronics)
