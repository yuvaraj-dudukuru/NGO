-- ============================================================
-- Case Study 2: Customer Analytics
-- File: data.sql  -- sample data
-- ============================================================

-- 5 registered customers, 2 Premium / 2 Regular among the active
-- ones, plus Karan (Premium) who has never ordered.
INSERT INTO Customers (CustomerID, CustomerName, Segment, City) VALUES
(1, 'Rajesh', 'Premium', 'Mumbai'),
(2, 'Priya',  'Regular', 'Delhi'),
(3, 'Aman',   'Premium', 'Bengaluru'),
(4, 'Sneha',  'Regular', 'Pune'),
(5, 'Karan',  'Premium', 'Hyderabad');

-- 6 orders from 4 customers (Karan has none -> he is "inactive").
INSERT INTO Orders (OrderID, CustomerID, ProductID, OrderAmount) VALUES
(1, 1, 1, 45000),   -- Rajesh
(2, 1, 2, 45000),   -- Rajesh
(3, 1, 3,  3600),   -- Rajesh
(4, 2, 1, 60000),   -- Priya
(5, 3, 2, 60000),   -- Aman
(6, 4, 1, 30000);   -- Sneha
