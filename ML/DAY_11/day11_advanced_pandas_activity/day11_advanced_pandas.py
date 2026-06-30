"""
Day 11 - Advanced Pandas: Complete Multi-Table Analysis (script version)
========================================================================
Plain-Python mirror of the Day11_Advanced_Pandas notebook. It walks the full
"combine and summarise" workflow an analyst uses every day, in 8 numbered steps:

    1. Load multiple datasets          5. Analyse the merged data
    2. GroupBy analysis                6. Pivot table (2-D summary)
    3. Multiple aggregations           7. KPI report
    4. Merge tables (join)             8. Crosstab (frequency counts)

Each step prints its result so you can follow exactly what every operation does.

Run:
    python day11_advanced_pandas.py
"""

import pandas as pd


def main():
    # ----------------------------------------------------------------------
    # Step 1 - Load multiple datasets
    # customers = the "who" (one row per customer); orders = the "what" (one row
    # per purchase). They share the CustomerID key, which lets us join them later.
    # ----------------------------------------------------------------------
    customers = pd.DataFrame({
        "CustomerID": [1, 2, 3, 4],
        "Name": ["Asha", "Ravi", "Imran", "Divya"],   # synthetic sample names
        "City": ["Pune", "Mumbai", "Pune", "Delhi"],
    })
    orders = pd.DataFrame({
        "OrderID": [101, 102, 103, 104, 105],
        "CustomerID": [1, 2, 1, 3, 4],
        "Category": ["Elec", "Groc", "Elec", "Cloth", "Groc"],
        "Amount": [25000, 1500, 30000, 9000, 2000],
    })
    print("Step 1 -customers:")
    print(customers)
    print("\nStep 1 -orders:")
    print(orders)

    # ----------------------------------------------------------------------
    # Step 2 - GroupBy analysis: collapse all orders of a category into one total.
    # ----------------------------------------------------------------------
    print("\nStep 2 -Revenue by category:")
    print(orders.groupby("Category")["Amount"].sum())

    # ----------------------------------------------------------------------
    # Step 3 - Multiple aggregations: compute total, average and count per
    # category in a single pass, with clear named output columns.
    # ----------------------------------------------------------------------
    print("\nStep 3 -Multi-aggregation by category:")
    print(orders.groupby("Category").agg(
        Total=("Amount", "sum"),
        Average=("Amount", "mean"),
        Count=("Amount", "count"),
    ).reset_index())

    # ----------------------------------------------------------------------
    # Step 4 - Merge tables: a LEFT join attaches each order's customer details
    # (Name, City) by matching on CustomerID. Now every order knows "who/where".
    # ----------------------------------------------------------------------
    merged = pd.merge(orders, customers, on="CustomerID", how="left")
    print("\nStep 4 -Merged table:")
    print(merged)

    # ----------------------------------------------------------------------
    # Step 5 - Analyse the merged data: revenue per city, ranked (only possible
    # *after* the join, because City lives in the customers table).
    # ----------------------------------------------------------------------
    print("\nStep 5 -Revenue by city (ranked):")
    print(merged.groupby("City")["Amount"].sum().sort_values(ascending=False))

    # ----------------------------------------------------------------------
    # Step 6 - Pivot table: a 2-D grid of City (rows) x Category (columns).
    # fill_value=0 shows empty combinations as 0; margins=True adds grand totals.
    # ----------------------------------------------------------------------
    pivot = pd.pivot_table(merged, index="City", columns="Category",
                           values="Amount", aggfunc="sum", fill_value=0, margins=True)
    print("\nStep 6 -Pivot table (City x Category):")
    print(pivot)

    # ----------------------------------------------------------------------
    # Step 7 - KPI report: total revenue and order count per city, ranked - the
    # kind of small table you would drop straight into a management dashboard.
    # ----------------------------------------------------------------------
    kpi = merged.groupby("City").agg(
        Total_Revenue=("Amount", "sum"),
        Orders=("OrderID", "count"),
    ).reset_index().sort_values("Total_Revenue", ascending=False)
    print("\nStep 7 -KPI report:")
    print(kpi)

    # ----------------------------------------------------------------------
    # Step 8 - Crosstab: counts *how many* orders fall in each City x Category
    # cell (frequency, not money) - good for spotting buying patterns.
    # ----------------------------------------------------------------------
    print("\nStep 8 -Crosstab (City x Category order counts):")
    print(pd.crosstab(merged["City"], merged["Category"]))


if __name__ == "__main__":
    main()
