-- ============================================================
-- Mini Project: NorthRetail
-- File: schema.sql  -- table definitions (PKs + FKs)
-- ============================================================

-- Start clean so the script can be re-run safely.
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Customers;

CREATE TABLE Customers (
    CustomerID   INTEGER PRIMARY KEY,
    CustomerName TEXT NOT NULL,
    City         TEXT NOT NULL
);

CREATE TABLE Products (
    ProductID   TEXT PRIMARY KEY,
    ProductName TEXT    NOT NULL,
    Category    TEXT    NOT NULL,
    Price       INTEGER NOT NULL
);

CREATE TABLE Orders (
    OrderID     INTEGER PRIMARY KEY,
    CustomerID  INTEGER NOT NULL,
    ProductID   TEXT    NOT NULL,
    Quantity    INTEGER NOT NULL,
    OrderAmount INTEGER NOT NULL,          -- = Quantity * Price
    OrderDate   TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID)  REFERENCES Products(ProductID)
);
