-- ============================================================
-- Case Study 1: Retail Sales Analysis
-- File: schema.sql  -- table definitions
-- ============================================================

-- Start clean so the script can be re-run safely.
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    CustomerID   INTEGER PRIMARY KEY,
    CustomerName TEXT    NOT NULL,
    Segment      TEXT    NOT NULL,   -- 'Premium' or 'Regular'
    City         TEXT
);

CREATE TABLE Products (
    ProductID   INTEGER PRIMARY KEY,
    ProductName TEXT    NOT NULL,
    Category    TEXT    NOT NULL     -- 'Electronics' or 'Accessories'
);

CREATE TABLE Orders (
    OrderID     INTEGER PRIMARY KEY,
    CustomerID  INTEGER NOT NULL,
    ProductID   INTEGER NOT NULL,
    OrderAmount INTEGER NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID)  REFERENCES Products(ProductID)
);
