"""
================================================================================
PHASE 5 — SQL ANALYSIS
================================================================================
Goal: Answer the SAME business questions using SQL (Day 9), proving the analysis
can be done directly in a database.

Flow: load the CLEANED DataFrame into an in-memory SQLite database, then query.
This bridges Pandas (Day 4) and SQL (Day 9). sqlite3 ships with Python.
================================================================================
"""

import sqlite3
import numpy as np
import pandas as pd


def get_clean_data():
    """Rebuild + clean the dataset so this file runs standalone (see Phase 2)."""
    df = pd.DataFrame({
        "OrderID":   [1001, 1002, 1003, 1003, 1005, 1006, 1007, 1008],
        "Customer":  ["asha", "RAVI", "Imran", "Imran", "Sneha", "Karan", "Meena", "Tara"],
        "City":      ["Pune", "mumbai", "Pune", "Pune", "Delhi", "Mumbai", "delhi", "Pune"],
        "Category":  ["Electronics", "Clothing", "Electronics", "Electronics",
                      "Grocery", "Electronics", "Clothing", "Grocery"],
        "Amount":    [25000, np.nan, 18000, 18000, 1200, 999999, 3200, 1500],
        "Quantity":  [2, 3, 1, 1, 5, 1, -2, 4],
        "OrderDate": ["2026-05-01", "2026-05-01", "2026-05-02", "2026-05-02",
                      "2026-05-03", "2026-05-03", "2026-05-04", "2026-05-05"],
    })
    df = df.drop_duplicates(subset=["OrderID"]).reset_index(drop=True)
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])
    df["Customer"] = df["Customer"].str.strip().str.title()
    df["City"] = df["City"].str.strip().str.title()
    mq = df.loc[df["Quantity"] > 0, "Quantity"].median()
    df["Quantity"] = df["Quantity"].astype(float)   # median may be a decimal (2.5)
    df.loc[df["Quantity"] < 0, "Quantity"] = mq
    Q1, Q3 = df["Amount"].quantile([0.25, 0.75])
    upper = Q3 + 1.5 * (Q3 - Q1)
    df.loc[df["Amount"] > upper, "Amount"] = np.nan
    df["Amount"] = df["Amount"].fillna(df["Amount"].median())
    return df


df = get_clean_data()

# ------------------------------------------------------------------------------
# 9.1  SETUP — load the cleaned DataFrame into SQLite
# ------------------------------------------------------------------------------
# ":memory:" = a temporary database that lives only in RAM (great for demos).
conn = sqlite3.connect(":memory:")
# to_sql writes our DataFrame into a SQL table named "sales".
df.to_sql("sales", conn, index=False, if_exists="replace")

# ------------------------------------------------------------------------------
# 9.2  DATA RETRIEVAL — "Show me all the cleaned orders."
# ------------------------------------------------------------------------------
print("9.2  All cleaned orders:")
print(pd.read_sql("SELECT * FROM sales", conn))

# ------------------------------------------------------------------------------
# 9.3  FILTERING — "Which orders are above Rs.10,000?"  (WHERE + ORDER BY)
# ------------------------------------------------------------------------------
print("\n9.3  High-value orders (> 10000):")
print(pd.read_sql(
    "SELECT Customer, Category, Amount FROM sales "
    "WHERE Amount > 10000 ORDER BY Amount DESC", conn))

# ------------------------------------------------------------------------------
# 9.4  SORTING — "Who placed the biggest orders?"
# ------------------------------------------------------------------------------
print("\n9.4  All orders ranked by amount:")
print(pd.read_sql(
    "SELECT Customer, City, Amount FROM sales ORDER BY Amount DESC", conn))

# ------------------------------------------------------------------------------
# 9.5  BUSINESS QUESTIONS  (GROUP BY + SUM — a preview of aggregation)
# ------------------------------------------------------------------------------
print("\n9.5a  Top category by total revenue:")
print(pd.read_sql(
    "SELECT Category, SUM(Amount) AS TotalRevenue FROM sales "
    "GROUP BY Category ORDER BY TotalRevenue DESC", conn))

print("\n9.5b  Highest-revenue city:")
print(pd.read_sql(
    "SELECT City, SUM(Amount) AS Revenue FROM sales "
    "GROUP BY City ORDER BY Revenue DESC", conn))

print("\n9.5c  Customers in Pune:")
print(pd.read_sql("SELECT Customer, Amount FROM sales WHERE City = 'Pune'", conn))

# Always close the connection when done.
conn.close()

print("""
Note: these SQL results MATCH the Pandas groupby() from Phase 3 — SQL and Pandas
reach the SAME insights. Real-world flow: SQL retrieves/filters at the database,
Pandas + charts refine and present.
""")
