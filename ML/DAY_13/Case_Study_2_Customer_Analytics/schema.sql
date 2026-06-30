-- ============================================================
-- Case Study 2: Customer Analytics
-- File: schema.sql  -- table definitions
-- ============================================================

-- Start clean so the script can be re-run safely.
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    CustomerID   INTEGER PRIMARY KEY,
    CustomerName TEXT    NOT NULL,
    Segment      TEXT    NOT NULL,   -- 'Premium' or 'Regular'
    City         TEXT
);

CREATE TABLE Orders (
    OrderID     INTEGER PRIMARY KEY,
    CustomerID  INTEGER NOT NULL,
    ProductID   INTEGER,
    OrderAmount INTEGER NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);
