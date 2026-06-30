"""
============================================================
Mini Project - NorthRetail Analytical SQL
============================================================
Role: data analyst at NorthRetail, a multi-category retailer.

This script designs a small relational database, populates it
with sample data, and produces a set of analytical business
reports using JOIN, GROUP BY and HAVING.

SQLite ships with Python (the `sqlite3` module). The only
external dependency is pandas for tidy table output.

Run:   python mini_project.py
Stop:  it finishes on its own; press Ctrl+C to abort early.
============================================================
"""

import sqlite3
import pandas as pd

# A customer is "high value" if they spend more than this.
SPEND_THRESHOLD = 50000


# ----------------------------------------------------------------
# 1 & 2. Design the tables and load the sample data
# ----------------------------------------------------------------
def build_database(conn):
    cur = conn.cursor()

    cur.executescript("""
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
            ProductName TEXT NOT NULL,
            Category    TEXT NOT NULL,
            Price       INTEGER NOT NULL
        );

        CREATE TABLE Orders (
            OrderID     INTEGER PRIMARY KEY,
            CustomerID  INTEGER NOT NULL,
            ProductID   TEXT NOT NULL,
            Quantity    INTEGER NOT NULL,
            OrderAmount INTEGER NOT NULL,
            OrderDate   TEXT,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
            FOREIGN KEY (ProductID)  REFERENCES Products(ProductID)
        );
    """)

    # 8 customers across 4 cities (2 each)
    customers = [
        (101, "Rajesh", "Hyderabad"),
        (102, "Priya",  "Bengaluru"),
        (103, "Aman",   "Mumbai"),
        (104, "Sneha",  "Delhi"),
        (105, "Karan",  "Hyderabad"),
        (106, "Meera",  "Bengaluru"),
        (107, "Vikram", "Mumbai"),
        (108, "Anita",  "Delhi"),
    ]

    # 5 products across 3 categories
    products = [
        ("P1", "Laptop",     "Electronics", 60000),
        ("P2", "Phone",      "Electronics", 30000),
        ("P3", "Headphones", "Accessories",  2000),
        ("P4", "Office Chair", "Furniture",  8000),
        ("P5", "Desk",       "Furniture",   12000),
    ]

    # 15 orders. OrderAmount = Quantity * Price (kept consistent).
    orders = [
        (5001, 101, "P1", 1, 60000, "2026-05-01"),
        (5002, 102, "P2", 2, 60000, "2026-05-02"),
        (5003, 101, "P3", 3,  6000, "2026-05-03"),
        (5004, 103, "P1", 1, 60000, "2026-05-04"),
        (5005, 104, "P2", 1, 30000, "2026-05-05"),
        (5006, 105, "P4", 2, 16000, "2026-05-06"),
        (5007, 106, "P5", 1, 12000, "2026-05-07"),
        (5008, 107, "P1", 1, 60000, "2026-05-08"),
        (5009, 108, "P2", 1, 30000, "2026-05-09"),
        (5010, 101, "P2", 1, 30000, "2026-05-10"),
        (5011, 102, "P3", 3,  6000, "2026-05-11"),
        (5012, 103, "P4", 1,  8000, "2026-05-12"),
        (5013, 105, "P1", 1, 60000, "2026-05-13"),
        (5014, 106, "P2", 2, 60000, "2026-05-14"),
        (5015, 107, "P5", 1, 12000, "2026-05-15"),
    ]

    cur.executemany("INSERT INTO Customers VALUES (?,?,?)", customers)
    cur.executemany("INSERT INTO Products  VALUES (?,?,?,?)", products)
    cur.executemany("INSERT INTO Orders    VALUES (?,?,?,?,?,?)", orders)
    conn.commit()


def section(title):
    print("\n" + "=" * 64)
    print(title)
    print("=" * 64)


def main():
    pd.set_option("display.width", 120)
    pd.set_option("display.max_columns", None)

    conn = sqlite3.connect(":memory:")
    conn.execute("PRAGMA foreign_keys = ON")   # enforce the foreign keys
    build_database(conn)
    print("Database built: 8 customers, 5 products, 15 orders.")

    # ------------------------------------------------------------
    # 3. Master join report (Orders + Customers + Products)
    # ------------------------------------------------------------
    section("3. MASTER REPORT (every order, fully described)")
    master = pd.read_sql("""
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
        ORDER BY o.OrderID
    """, conn)
    print(master.to_string(index=False))

    # ------------------------------------------------------------
    # 4. KPIs
    # ------------------------------------------------------------
    section("4. KEY PERFORMANCE INDICATORS")
    kpis = pd.read_sql("""
        SELECT COUNT(*)                   AS Orders,
               COUNT(DISTINCT CustomerID) AS Customers,
               SUM(OrderAmount)           AS Revenue,
               AVG(OrderAmount)           AS AvgOrderValue
        FROM Orders
    """, conn)
    print(kpis.to_string(index=False))

    # ------------------------------------------------------------
    # 5a. Revenue by category, ranked descending
    # ------------------------------------------------------------
    section("5a. REVENUE BY CATEGORY (ranked)")
    category = pd.read_sql("""
        SELECT p.Category,
               SUM(o.OrderAmount) AS Revenue,
               COUNT(*)           AS Orders
        FROM Orders o
        INNER JOIN Products p ON o.ProductID = p.ProductID
        GROUP BY p.Category
        ORDER BY Revenue DESC
    """, conn)
    print(category.to_string(index=False))

    # ------------------------------------------------------------
    # 5b. High-value customers (GROUP BY + HAVING)
    # ------------------------------------------------------------
    section(f"5b. HIGH-VALUE CUSTOMERS (spend > {SPEND_THRESHOLD:,})")
    high_value = pd.read_sql("""
        SELECT c.CustomerName,
               c.City,
               COUNT(*)           AS Orders,
               SUM(o.OrderAmount) AS TotalSpent
        FROM Customers c
        INNER JOIN Orders o ON c.CustomerID = o.CustomerID
        GROUP BY c.CustomerID, c.CustomerName, c.City
        HAVING SUM(o.OrderAmount) > ?
        ORDER BY TotalSpent DESC
    """, conn, params=(SPEND_THRESHOLD,))
    print(high_value.to_string(index=False))

    # ------------------------------------------------------------
    # 5c. Orders and revenue by city
    # ------------------------------------------------------------
    section("5c. ORDERS & REVENUE BY CITY")
    city = pd.read_sql("""
        SELECT c.City,
               COUNT(*)           AS Orders,
               SUM(o.OrderAmount) AS Revenue
        FROM Customers c
        INNER JOIN Orders o ON c.CustomerID = o.CustomerID
        GROUP BY c.City
        ORDER BY Revenue DESC
    """, conn)
    print(city.to_string(index=False))

    # ------------------------------------------------------------
    # 5d. Best-selling products by total quantity
    # ------------------------------------------------------------
    section("5d. BEST-SELLING PRODUCTS (by units sold)")
    best = pd.read_sql("""
        SELECT p.ProductName,
               p.Category,
               SUM(o.Quantity)    AS UnitsSold,
               SUM(o.OrderAmount) AS Revenue
        FROM Products p
        INNER JOIN Orders o ON p.ProductID = o.ProductID
        GROUP BY p.ProductID, p.ProductName, p.Category
        ORDER BY UnitsSold DESC
    """, conn)
    print(best.to_string(index=False))

    # ------------------------------------------------------------
    # 6. Documented findings (derived from the reports above)
    # ------------------------------------------------------------
    section("6. FINDINGS & RECOMMENDATIONS")
    total_rev = int(kpis.loc[0, "Revenue"])
    top_cat = category.iloc[0]
    top_cust = high_value.iloc[0]
    top_city = city.iloc[0]
    top_units = best.iloc[0]
    top_rev_prod = best.sort_values("Revenue", ascending=False).iloc[0]

    print(f"- Total revenue is {total_rev:,} across {int(kpis.loc[0,'Orders'])} orders "
          f"from {int(kpis.loc[0,'Customers'])} customers "
          f"(avg order value {kpis.loc[0,'AvgOrderValue']:,.0f}).")
    print(f"- Top category: {top_cat['Category']} at {int(top_cat['Revenue']):,} "
          f"({top_cat['Revenue'] / total_rev:.1%} of revenue).")
    print(f"- Strongest city: {top_city['City']} at {int(top_city['Revenue']):,} "
          f"across {int(top_city['Orders'])} orders.")
    print(f"- Top customer: {top_cust['CustomerName']} ({top_cust['City']}) "
          f"at {int(top_cust['TotalSpent']):,}; "
          f"{len(high_value)} customers exceed the {SPEND_THRESHOLD:,} threshold.")
    print(f"- Best seller by volume: {top_units['ProductName']} "
          f"({int(top_units['UnitsSold'])} units), but the top revenue product is "
          f"{top_rev_prod['ProductName']} ({int(top_rev_prod['Revenue']):,}).")
    print()
    print("Recommendations:")
    print("  1. Concentrate inventory and supplier deals on Electronics - it dominates revenue.")
    print("  2. Run a loyalty / targeted-offer programme for the high-value customers above.")
    print(f"  3. Invest in the strongest market ({top_city['City']}) and investigate the "
          "weakest city for a re-engagement campaign.")
    print("  4. Phones sell in the highest volume while laptops drive the most revenue - "
          "bundle accessories with phones and upsell laptops to lift the smaller categories.")

    conn.close()
    print("\nConnection closed.")


if __name__ == "__main__":
    main()
