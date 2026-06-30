"""
============================================================
Day 13 - Hands-On Activity: SQLite through Python
============================================================
The complete analytical SQL workflow in one script:
build a schema, populate it, JOIN, aggregate, GROUP BY,
HAVING, and produce a business report.

SQLite ships with Python (the `sqlite3` module), so the
only external dependency is pandas for tidy table output.

Run:   python hands_on_activity.py
Stop:  it finishes on its own; press Ctrl+C to abort early.
============================================================
"""

import sqlite3
import pandas as pd


def main():
    # ----------------------------------------------------------------
    # Step 1 - Connect to a database and create the cursor
    # ----------------------------------------------------------------
    # ":memory:" creates a throwaway database that lives only in RAM,
    # so nothing is written to disk and there is no file to clean up.
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    print("Database connection established.\n")

    # ----------------------------------------------------------------
    # Step 2 - Create the tables (define the relational schema)
    # ----------------------------------------------------------------
    cursor.execute("""
        CREATE TABLE Customers (
            CustomerID   INTEGER PRIMARY KEY,
            CustomerName TEXT,
            City         TEXT,
            Segment      TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE Products (
            ProductID   TEXT PRIMARY KEY,
            ProductName TEXT,
            Category    TEXT,
            Price       INTEGER
        )
    """)

    cursor.execute("""
        CREATE TABLE Orders (
            OrderID     INTEGER PRIMARY KEY,
            CustomerID  INTEGER,
            ProductID   TEXT,
            Quantity    INTEGER,
            OrderAmount INTEGER,
            OrderDate   TEXT
        )
    """)
    print("Tables created.\n")

    # ----------------------------------------------------------------
    # Step 3 - Populate the tables (insert the sample data)
    # ----------------------------------------------------------------
    customers = [
        (101, "Rajesh", "Hyderabad", "Premium"),
        (102, "Priya",  "Bengaluru", "Regular"),
        (103, "Aman",   "Mumbai",    "Premium"),
        (104, "Sneha",  "Delhi",     "Regular"),
        (105, "Karan",  "Hyderabad", "Premium"),
    ]
    products = [
        ("P1", "Laptop", "Electronics", 60000),
        ("P2", "Phone",  "Electronics", 30000),
        ("P3", "Mouse",  "Accessories", 1200),
    ]
    orders = [
        (5001, 101, "P1", 1, 60000, "2026-05-01"),
        (5002, 102, "P2", 2, 60000, "2026-05-02"),
        (5003, 101, "P3", 3,  3600, "2026-05-03"),
        (5004, 103, "P1", 1, 60000, "2026-05-05"),
        (5005, 104, "P2", 1, 30000, "2026-05-07"),
        (5006, 101, "P2", 1, 30000, "2026-05-09"),
    ]

    cursor.executemany("INSERT INTO Customers VALUES (?,?,?,?)", customers)
    cursor.executemany("INSERT INTO Products  VALUES (?,?,?,?)", products)
    cursor.executemany("INSERT INTO Orders    VALUES (?,?,?,?,?,?)", orders)
    conn.commit()
    print("Sample data inserted.\n")

    # ----------------------------------------------------------------
    # Step 4 - Perform an INNER JOIN
    # ----------------------------------------------------------------
    query = """
        SELECT c.CustomerName, o.OrderAmount
        FROM Customers c
        INNER JOIN Orders o ON c.CustomerID = o.CustomerID
    """
    print("Step 4 - INNER JOIN (customer name + each order amount):")
    print(pd.read_sql(query, conn), "\n")

    # ----------------------------------------------------------------
    # Step 5 - Use aggregate functions
    # ----------------------------------------------------------------
    query = """
        SELECT COUNT(*)         AS Orders,
               SUM(OrderAmount) AS Revenue,
               AVG(OrderAmount) AS AvgValue
        FROM Orders
    """
    print("Step 5 - Aggregates over all orders:")
    print(pd.read_sql(query, conn), "\n")

    # ----------------------------------------------------------------
    # Step 6 - Apply GROUP BY
    # ----------------------------------------------------------------
    query = """
        SELECT CustomerID, SUM(OrderAmount) AS TotalSpent
        FROM Orders
        GROUP BY CustomerID
        ORDER BY TotalSpent DESC
    """
    print("Step 6 - Total spend per customer (GROUP BY):")
    print(pd.read_sql(query, conn), "\n")

    # ----------------------------------------------------------------
    # Step 7 - Apply HAVING (filter groups after aggregation)
    # ----------------------------------------------------------------
    query = """
        SELECT CustomerID, SUM(OrderAmount) AS TotalSpent
        FROM Orders
        GROUP BY CustomerID
        HAVING SUM(OrderAmount) > 50000
    """
    print("Step 7 - Customers who spent more than 50,000 (HAVING):")
    print(pd.read_sql(query, conn), "\n")

    # ----------------------------------------------------------------
    # Step 8 - Generate a complete report and close the connection
    # ----------------------------------------------------------------
    query = """
        SELECT c.CustomerName, c.City, SUM(o.OrderAmount) AS TotalSpent
        FROM Customers c
        INNER JOIN Orders o ON c.CustomerID = o.CustomerID
        GROUP BY c.CustomerName, c.City
        HAVING SUM(o.OrderAmount) > 50000
        ORDER BY TotalSpent DESC
    """
    report = pd.read_sql(query, conn)
    print("Step 8 - Business report (high-value customers):")
    print(report, "\n")

    conn.close()
    print("Connection closed.")


if __name__ == "__main__":
    main()
