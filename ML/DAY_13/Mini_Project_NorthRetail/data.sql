-- ============================================================
-- Mini Project: NorthRetail
-- File: data.sql  -- sample data
-- 8 customers (4 cities), 5 products (3 categories), 15 orders.
-- ============================================================

INSERT INTO Customers (CustomerID, CustomerName, City) VALUES
(101, 'Rajesh', 'Hyderabad'),
(102, 'Priya',  'Bengaluru'),
(103, 'Aman',   'Mumbai'),
(104, 'Sneha',  'Delhi'),
(105, 'Karan',  'Hyderabad'),
(106, 'Meera',  'Bengaluru'),
(107, 'Vikram', 'Mumbai'),
(108, 'Anita',  'Delhi');

INSERT INTO Products (ProductID, ProductName, Category, Price) VALUES
('P1', 'Laptop',       'Electronics', 60000),
('P2', 'Phone',        'Electronics', 30000),
('P3', 'Headphones',   'Accessories',  2000),
('P4', 'Office Chair', 'Furniture',    8000),
('P5', 'Desk',         'Furniture',   12000);

-- OrderAmount = Quantity * Price (kept consistent on purpose).
INSERT INTO Orders (OrderID, CustomerID, ProductID, Quantity, OrderAmount, OrderDate) VALUES
(5001, 101, 'P1', 1, 60000, '2026-05-01'),
(5002, 102, 'P2', 2, 60000, '2026-05-02'),
(5003, 101, 'P3', 3,  6000, '2026-05-03'),
(5004, 103, 'P1', 1, 60000, '2026-05-04'),
(5005, 104, 'P2', 1, 30000, '2026-05-05'),
(5006, 105, 'P4', 2, 16000, '2026-05-06'),
(5007, 106, 'P5', 1, 12000, '2026-05-07'),
(5008, 107, 'P1', 1, 60000, '2026-05-08'),
(5009, 108, 'P2', 1, 30000, '2026-05-09'),
(5010, 101, 'P2', 1, 30000, '2026-05-10'),
(5011, 102, 'P3', 3,  6000, '2026-05-11'),
(5012, 103, 'P4', 1,  8000, '2026-05-12'),
(5013, 105, 'P1', 1, 60000, '2026-05-13'),
(5014, 106, 'P2', 2, 60000, '2026-05-14'),
(5015, 107, 'P5', 1, 12000, '2026-05-15');
