"""
Mini Challenge - ShopVerse Multi-Table Business Analysis
=========================================================
Senior-analyst task: merge three related tables (orders + customers + products),
engineer a Revenue column, then produce pivot tables, KPI reports, a crosstab,
and business insights.

Covers: multi-table joins, feature engineering, pivot_table, groupby KPIs,
idxmax, crosstab, and (stretch) average order value + a Seaborn revenue chart.
"""

import pandas as pd


def build_tables():
    """Return the customers, products, and orders DataFrames."""
    customers = pd.DataFrame({
        "CustomerID": [1, 2, 3, 4, 5],
        "Name": ["Asha", "Ravi", "Imran", "Divya", "Karan"],
        "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai"],
        "Segment": ["Premium", "Regular", "Premium", "Regular", "Premium"],
    })
    products = pd.DataFrame({
        "ProductID": ["P1", "P2", "P3"],
        "Product": ["Laptop", "Phone", "Headphones"],
        "Category": ["Electronics", "Electronics", "Accessories"],
        "Price": [60000, 30000, 3000],
    })
    orders = pd.DataFrame({
        "OrderID": [101, 102, 103, 104, 105, 106, 107, 108],
        "CustomerID": [1, 2, 1, 3, 4, 5, 1, 3],
        "ProductID": ["P1", "P2", "P3", "P1", "P2", "P1", "P2", "P3"],
        "Quantity": [1, 2, 3, 1, 1, 1, 2, 5],
    })
    return customers, products, orders


def build_full(customers, products, orders):
    """Merge all three tables and add a Revenue column (Quantity * Price).

    Two chained left joins enrich each order with its customer details (Name,
    City, Segment) and its product details (Product, Category, Price). Revenue is
    an *engineered* feature: it does not exist in any source table - we derive it
    from Quantity x Price so we can total and rank money.
    """
    step1 = pd.merge(orders, customers, on="CustomerID", how="left")
    full = pd.merge(step1, products, on="ProductID", how="left")
    full["Revenue"] = full["Quantity"] * full["Price"]
    return full


# ----- 2. Pivot tables (2-D summaries) -----
def pivot_city_category(full):
    """Revenue grid: City (rows) x Category (columns), with grand-total margins."""
    return pd.pivot_table(full, index="City", columns="Category",
                          values="Revenue", aggfunc="sum", fill_value=0, margins=True)


def pivot_segment_product(full):
    """Revenue grid: Segment (rows) x Product (columns) - what each tier buys."""
    return pd.pivot_table(full, index="Segment", columns="Product",
                          values="Revenue", aggfunc="sum", fill_value=0)


# ----- 3. KPI reports (one number per group) -----
def revenue_by_city(full):
    """Total revenue per city, highest first."""
    return full.groupby("City")["Revenue"].sum().sort_values(ascending=False)


def revenue_by_segment(full):
    """Total revenue per customer segment (Premium vs Regular)."""
    return full.groupby("Segment")["Revenue"].sum()


def top_customer(full):
    """Name of the single highest-revenue customer (idxmax = label of the max)."""
    return full.groupby("Name")["Revenue"].sum().idxmax()


def revenue_by_category(full):
    """Total revenue per product category."""
    return full.groupby("Category")["Revenue"].sum()


# ----- 4. Crosstab (frequency, not money) -----
def orders_crosstab(full):
    """Count how many orders fall in each City x Category cell."""
    return pd.crosstab(full["City"], full["Category"])


# ----- Stretch: average order value per segment -----
def avg_order_value_by_segment(full):
    """Mean revenue per order within each segment (spend per transaction)."""
    return full.groupby("Segment")["Revenue"].mean()


def save_revenue_chart(full, path):
    """Stretch goal: Seaborn bar chart of revenue by city. Skips if libs missing."""
    try:
        import matplotlib
        matplotlib.use("Agg")  # headless, no display needed
        import matplotlib.pyplot as plt
        import seaborn as sns
    except ImportError:
        print(f"(Chart skipped - seaborn/matplotlib not installed: {path} not written)")
        return False

    city_rev = revenue_by_city(full).reset_index()
    plt.figure(figsize=(7, 4))
    sns.barplot(data=city_rev, x="City", y="Revenue", hue="City",
                palette="viridis", legend=False)
    plt.title("Revenue by City - ShopVerse")
    plt.ylabel("Revenue (Rs)")
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()
    print(f"(Chart saved to {path})")
    return True


def main():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 120)

    customers, products, orders = build_tables()
    full = build_full(customers, products, orders)

    print("=== 1. Merged analysis dataset ===")
    print(full[["OrderID", "Name", "City", "Segment", "Product",
                "Category", "Quantity", "Price", "Revenue"]])

    print("\n=== 2a. Pivot: Revenue by City x Category (with totals) ===")
    print(pivot_city_category(full))

    print("\n=== 2b. Pivot: Revenue by Segment x Product ===")
    print(pivot_segment_product(full))

    print("\n=== 3a. Total revenue by city (desc) ===")
    print(revenue_by_city(full))

    print("\n=== 3b. Total revenue by segment ===")
    print(revenue_by_segment(full))

    print("\n=== 3c. Top customer by total revenue ===")
    print("Top customer:", top_customer(full))

    print("\n=== 3d. Total revenue by product category ===")
    print(revenue_by_category(full))

    print("\n=== 4. Crosstab: order count by City x Category ===")
    print(orders_crosstab(full))

    print("\n=== Stretch: average order value by segment ===")
    print(avg_order_value_by_segment(full))

    print()
    save_revenue_chart(full, "revenue_by_city.png")


if __name__ == "__main__":
    main()
