"""
Business Analytics Case Study 1 - Retail Sales
================================================
Applies GroupBy, multi-aggregation, and pivot tables to a realistic retail dataset.

Business context:
    A retailer wants a quick read on performance: which region earns the most,
    what each product category contributes, and how revenue splits across the
    region x category grid.

Concepts demonstrated:
    * groupby(col)["x"].sum()  - one total per group
    * groupby(col).agg(...)    - several KPIs at once with named output columns
    * pd.pivot_table(...)      - a 2-D summary (rows x columns) with row/col totals

Run:
    python retail_sales_analysis.py
"""

import pandas as pd


def build_dataset():
    """Return the retail sales table - one row per (region, category) sale.

    Hard-coded so the script is self-contained and reproducible.
    """
    return pd.DataFrame({
        "Region": ["North", "South", "East", "North", "South", "East", "North", "East"],
        "Category": ["Elec", "Groc", "Elec", "Cloth", "Elec", "Groc", "Elec", "Cloth"],
        "Units": [5, 20, 8, 15, 6, 25, 10, 12],
        "Revenue": [50000, 12000, 60000, 9000, 55000, 14000, 80000, 7000],
    })


def revenue_by_region(sales):
    """Total revenue per region, ranked - the single most-asked sales question."""
    # groupby collapses all rows of a region into one; sum() totals their Revenue.
    return sales.groupby("Region")["Revenue"].sum().sort_values(ascending=False)


def kpis_by_category(sales):
    """Three KPIs per category at once: total revenue, average revenue, total units.

    .agg() with name=("column", "function") pairs produces tidy, clearly named
    output columns instead of a confusing multi-level header.
    """
    return sales.groupby("Category").agg(
        Total_Revenue=("Revenue", "sum"),
        Avg_Revenue=("Revenue", "mean"),
        Total_Units=("Units", "sum"),
    ).reset_index()


def region_category_pivot(sales):
    """Revenue laid out as Region (rows) x Category (columns).

    margins=True adds an 'All' row and column (the grand totals); fill_value=0
    replaces empty cells (combinations with no sales) with 0 instead of NaN.
    """
    return pd.pivot_table(
        sales,
        index="Region",
        columns="Category",
        values="Revenue",
        aggfunc="sum",
        fill_value=0,
        margins=True,
    )


def main():
    sales = build_dataset()

    print("Revenue by region:")
    print(revenue_by_region(sales))

    print("\nFull KPIs by category:")
    print(kpis_by_category(sales))

    print("\nRevenue pivot (Region x Category):")
    print(region_category_pivot(sales))

    # Expected insight:
    #   North leads on revenue (driven by high-value Electronics), and Electronics
    #   is the top category overall. The pivot shows Grocery sells many Units but
    #   little Revenue - useful for separating "popular" from "profitable".


if __name__ == "__main__":
    main()
