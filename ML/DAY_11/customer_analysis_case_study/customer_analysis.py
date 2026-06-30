"""
Business Analytics Case Study 2 - Customer Analysis
====================================================
Showcases MERGING (joins) for customer segmentation and revenue analysis.

Business context:
    Order records only store a CustomerID - not the customer's name, city, or
    segment. To analyse *who* spends the most (and where), we must first JOIN the
    orders table to the customers table, then group the combined data.

Concepts demonstrated:
    * pd.merge(...)            - combine two tables on a shared key (CustomerID)
    * groupby(...).sum()       - aggregate a numeric column within each group
    * sort_values(...)         - rank the result
    * segmentation             - compare Premium vs Regular customers

Run:
    python customer_analysis.py
"""

import pandas as pd


def build_tables():
    """Return the two raw source tables: customers (the 'who') and orders (the 'what').

    In a real project these would be loaded from a database or CSV; here they are
    hard-coded so the script is fully self-contained and reproducible.
    """
    # One row per customer. 'Segment' marks high-value (Premium) vs ordinary (Regular).
    customers = pd.DataFrame({
        "CustomerID": [1, 2, 3, 4],
        "Name": ["Asha", "Ravi", "Imran", "Divya"],   # synthetic sample names
        "City": ["Pune", "Mumbai", "Pune", "Delhi"],
        "Segment": ["Premium", "Regular", "Premium", "Regular"],
    })
    # One row per order. Note CustomerID 1 (Asha) appears 3 times - a repeat buyer.
    orders = pd.DataFrame({
        "OrderID": [101, 102, 103, 104, 105, 106],
        "CustomerID": [1, 2, 1, 3, 4, 1],
        "Amount": [25000, 1500, 30000, 18000, 2000, 12000],
    })
    return customers, orders


def merge_tables(orders, customers):
    """LEFT-join every order onto its customer's details.

    how="left" keeps every order even if a matching customer were missing, so we
    never silently drop sales. After this each order row also carries Name, City,
    and Segment - ready for grouping.
    """
    return pd.merge(orders, customers, on="CustomerID", how="left")


def spending_by_customer(merged):
    """Total spend per customer, highest first (identifies the most valuable buyers)."""
    return merged.groupby("Name")["Amount"].sum().sort_values(ascending=False)


def revenue_by_segment(merged):
    """Total revenue per segment - quantifies how much Premium customers are worth."""
    return merged.groupby("Segment")["Amount"].sum()


def revenue_by_city(merged):
    """Total revenue per city - shows which market generates the most sales."""
    return merged.groupby("City")["Amount"].sum()


def main():
    # 1) Build the raw tables, then 2) join them into one analysis-ready table.
    customers, orders = build_tables()
    merged = merge_tables(orders, customers)

    # 3) Answer three business questions off the joined data.
    print("Total spending by customer:")
    print(spending_by_customer(merged))

    print("\nRevenue by segment:")
    print(revenue_by_segment(merged))

    print("\nRevenue by city:")
    print(revenue_by_city(merged))

    # Expected insight:
    #   Asha (Premium, Pune) is the top spender at 67,000 across 3 orders.
    #   Premium customers far out-earn Regular ones, and Pune is the strongest
    #   city - so loyalty perks aimed at Premium buyers in Pune should pay off.


if __name__ == "__main__":
    main()
