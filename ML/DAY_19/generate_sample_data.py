"""
generate_sample_data.py
========================
Generates the SYNTHETIC sample datasets used by the three Day 19 dashboard
case studies (Sales, Customer Analytics, HR).

No real or personal data is used. Every record is randomly generated from
fixed distributions with a fixed random seed, so the output is reproducible.
Identifiers are synthetic codes (e.g. ORD-00001, CUST-00001, EMP-001) and
no names, emails, or other personal information are produced.

For each case study the script writes two files into its ``data`` folder:
  * <name>.csv  -> import this into Power BI / Tableau
  * <name>.js   -> embedded by the offline HTML dashboard (window.<NAME>_DATA)

Run:  python generate_sample_data.py
"""

import csv
import json
import os
import random
from datetime import date, timedelta

SEED = 42
ROOT = os.path.dirname(os.path.abspath(__file__))


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def write_outputs(folder, base_name, js_var, rows, fieldnames):
    """Write rows to both a .csv and a .js file inside ``folder``/data."""
    data_dir = os.path.join(ROOT, folder, "data")
    os.makedirs(data_dir, exist_ok=True)

    csv_path = os.path.join(data_dir, base_name + ".csv")
    with open(csv_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    js_path = os.path.join(data_dir, base_name + ".js")
    with open(js_path, "w", encoding="utf-8") as fh:
        fh.write("/* Auto-generated synthetic data. Do not edit by hand. */\n")
        fh.write("window.%s = " % js_var)
        json.dump(rows, fh, separators=(",", ":"))
        fh.write(";\n")

    print("  wrote %-22s (%d rows)" % (base_name + ".csv/.js", len(rows)))


def daterange(start, end):
    """Return a list of every date from start to end inclusive (one per day)."""
    days = (end - start).days
    return [start + timedelta(days=i) for i in range(days + 1)]


# --------------------------------------------------------------------------
# Case Study 1 - Sales
# --------------------------------------------------------------------------
def generate_sales():
    """Build the Case Study 1 sales dataset (daily orders with regional + seasonal patterns)."""
    rnd = random.Random(SEED)

    # East intentionally leads the market; South is the weakest.
    regions = {"East": 0.34, "West": 0.27, "North": 0.22, "South": 0.17}

    # category -> (products, base_price, margin_pct)
    catalogue = {
        "Electronics": (["Laptop", "Smartphone", "Headphones", "Monitor"], 650, 0.32),
        "Furniture": (["Office Chair", "Desk", "Bookshelf", "Cabinet"], 320, 0.40),
        "Office Supplies": (["Printer Paper", "Stapler", "Notebook", "Pen Set"], 28, 0.55),
        "Clothing": (["Jacket", "T-Shirt", "Shoes", "Backpack"], 75, 0.48),
    }
    cat_weights = {"Electronics": 0.42, "Furniture": 0.24,
                   "Office Supplies": 0.18, "Clothing": 0.16}

    start = date(2023, 1, 1)
    end = date(2024, 12, 31)
    all_days = daterange(start, end)

    # monthly seasonality multiplier (peak in Nov/Dec holiday season, summer dip)
    season = {1: 0.85, 2: 0.82, 3: 0.95, 4: 1.00, 5: 1.05, 6: 0.92,
              7: 0.88, 8: 0.95, 9: 1.08, 10: 1.15, 11: 1.35, 12: 1.45}

    def day_weight(d):
        # upward trend across the two years + seasonality
        trend = 1.0 + (d - start).days / all_days.__len__() * 0.6
        return trend * season[d.month]

    weights = [day_weight(d) for d in all_days]

    region_names = list(regions)
    region_w = list(regions.values())
    cat_names = list(cat_weights)
    cat_w = list(cat_weights.values())

    rows = []
    n_orders = 2600
    for i in range(1, n_orders + 1):
        d = rnd.choices(all_days, weights=weights, k=1)[0]
        region = rnd.choices(region_names, weights=region_w, k=1)[0]
        category = rnd.choices(cat_names, weights=cat_w, k=1)[0]
        products, base_price, margin = catalogue[category]
        product = rnd.choice(products)

        unit_price = round(base_price * rnd.uniform(0.6, 1.8), 2)
        unit_cost = round(unit_price * (1 - margin) * rnd.uniform(0.9, 1.1), 2)
        quantity = rnd.randint(1, 8)

        revenue = round(unit_price * quantity, 2)
        profit = round((unit_price - unit_cost) * quantity, 2)

        rows.append({
            "OrderID": "ORD-%05d" % i,
            "Date": d.isoformat(),
            "Region": region,
            "ProductCategory": category,
            "Product": product,
            "Quantity": quantity,
            "UnitPrice": unit_price,
            "UnitCost": unit_cost,
            "Revenue": revenue,
            "Profit": profit,
        })

    rows.sort(key=lambda r: r["Date"])
    fieldnames = ["OrderID", "Date", "Region", "ProductCategory", "Product",
                  "Quantity", "UnitPrice", "UnitCost", "Revenue", "Profit"]
    write_outputs("Case_Study_1_Sales_Dashboard", "sales_data",
                  "SALES_DATA", rows, fieldnames)


# --------------------------------------------------------------------------
# Case Study 2 - Customers
# --------------------------------------------------------------------------
def generate_customers():
    """Build the Case Study 2 customer dataset (segments, signup dates, retention)."""
    rnd = random.Random(SEED + 1)

    # Premium: few customers, high value, high retention.
    segments = {
        "Premium": {"weight": 0.18, "rev": (4000, 12000), "orders": (12, 40), "retain": 0.90},
        "Standard": {"weight": 0.42, "rev": (1200, 4500), "orders": (5, 18), "retain": 0.72},
        "Basic": {"weight": 0.40, "rev": (150, 1200), "orders": (1, 6), "retain": 0.48},
    }
    regions = {"East": 0.30, "West": 0.26, "North": 0.24, "South": 0.20}

    start = date(2023, 1, 1)
    end = date(2024, 12, 31)
    all_days = daterange(start, end)

    # accelerating acquisition: later dates much more likely
    weights = [(1.0 + (d - start).days / len(all_days) * 2.0) ** 1.6 for d in all_days]

    seg_names = list(segments)
    seg_w = [segments[s]["weight"] for s in seg_names]
    reg_names = list(regions)
    reg_w = list(regions.values())

    rows = []
    n = 900
    for i in range(1, n + 1):
        seg = rnd.choices(seg_names, weights=seg_w, k=1)[0]
        cfg = segments[seg]
        signup = rnd.choices(all_days, weights=weights, k=1)[0]
        region = rnd.choices(reg_names, weights=reg_w, k=1)[0]
        revenue = round(rnd.uniform(*cfg["rev"]), 2)
        orders = rnd.randint(*cfg["orders"])
        retained = 1 if rnd.random() < cfg["retain"] else 0

        rows.append({
            "CustomerID": "CUST-%05d" % i,
            "SignupDate": signup.isoformat(),
            "Region": region,
            "Segment": seg,
            "TotalRevenue": revenue,
            "Orders": orders,
            "Retained": retained,
        })

    rows.sort(key=lambda r: r["SignupDate"])
    fieldnames = ["CustomerID", "SignupDate", "Region", "Segment",
                  "TotalRevenue", "Orders", "Retained"]
    write_outputs("Case_Study_2_Customer_Analytics_Dashboard", "customer_data",
                  "CUSTOMER_DATA", rows, fieldnames)


# --------------------------------------------------------------------------
# Case Study 3 - HR
# --------------------------------------------------------------------------
def generate_hr():
    """Build the Case Study 3 HR dataset (departments, performance, tenure)."""
    rnd = random.Random(SEED + 2)

    # department -> (headcount weight, mean performance, perf spread, mean tenure)
    departments = {
        "Engineering": (0.26, 82, 9, 4.5),   # highest performing
        "Sales": (0.22, 74, 12, 3.2),
        "Marketing": (0.14, 71, 11, 3.0),
        "Operations": (0.18, 64, 10, 5.0),   # lagging department
        "Finance": (0.10, 76, 8, 5.5),
        "HR": (0.10, 73, 9, 4.0),
    }

    dep_names = list(departments)
    dep_w = [departments[d][0] for d in dep_names]

    def perf_category(score):
        if score >= 80:
            return "High"
        if score >= 60:
            return "Medium"
        return "Low"

    rows = []
    n = 320
    for i in range(1, n + 1):
        dep = rnd.choices(dep_names, weights=dep_w, k=1)[0]
        _, mean_perf, spread, mean_tenure = departments[dep]
        score = int(max(35, min(99, rnd.gauss(mean_perf, spread))))
        tenure = round(max(0.2, rnd.gauss(mean_tenure, 1.8)), 1)

        rows.append({
            "EmployeeID": "EMP-%03d" % i,
            "Department": dep,
            "PerformanceScore": score,
            "PerformanceCategory": perf_category(score),
            "TenureYears": tenure,
        })

    fieldnames = ["EmployeeID", "Department", "PerformanceScore",
                  "PerformanceCategory", "TenureYears"]
    write_outputs("Case_Study_3_HR_Dashboard", "hr_data",
                  "HR_DATA", rows, fieldnames)


# --------------------------------------------------------------------------
# Hands-On Activity - generic sales dataset
# Columns exactly as named in the activity brief:
#   Region, Product, Category, Sales, Profit, Date (+ OrderID, Quantity)
# --------------------------------------------------------------------------
def generate_handson():
    """Build the Hands-On Activity sales dataset (a separate region leader: West)."""
    rnd = random.Random(SEED + 3)

    # West leads here (a different leader than Case Study 1, to keep it distinct).
    regions = {"West": 0.33, "East": 0.26, "Central": 0.23, "South": 0.18}

    # category -> (products, base_price, margin_pct)
    catalogue = {
        "Technology": (["Laptops", "Phones", "Accessories"], 540, 0.30),
        "Furniture": (["Chairs", "Tables", "Bookcases"], 300, 0.38),
        "Office Supplies": (["Binders", "Paper", "Art Supplies"], 24, 0.52),
    }
    cat_weights = {"Technology": 0.45, "Furniture": 0.30, "Office Supplies": 0.25}

    start = date(2023, 1, 1)
    end = date(2024, 12, 31)
    all_days = daterange(start, end)

    season = {1: 0.88, 2: 0.85, 3: 0.97, 4: 1.02, 5: 1.06, 6: 0.95,
              7: 0.90, 8: 0.98, 9: 1.10, 10: 1.18, 11: 1.30, 12: 1.40}

    def day_weight(d):
        trend = 1.0 + (d - start).days / len(all_days) * 0.7
        return trend * season[d.month]

    weights = [day_weight(d) for d in all_days]
    region_names = list(regions); region_w = list(regions.values())
    cat_names = list(cat_weights); cat_w = list(cat_weights.values())

    rows = []
    n_orders = 2000
    for i in range(1, n_orders + 1):
        d = rnd.choices(all_days, weights=weights, k=1)[0]
        region = rnd.choices(region_names, weights=region_w, k=1)[0]
        category = rnd.choices(cat_names, weights=cat_w, k=1)[0]
        products, base_price, margin = catalogue[category]
        product = rnd.choice(products)

        unit_price = base_price * rnd.uniform(0.6, 1.8)
        quantity = rnd.randint(1, 9)
        sales = round(unit_price * quantity, 2)
        profit = round(sales * margin * rnd.uniform(0.7, 1.2), 2)

        rows.append({
            "OrderID": "ORD-%05d" % i,
            "Date": d.isoformat(),
            "Region": region,
            "Category": category,
            "Product": product,
            "Quantity": quantity,
            "Sales": sales,
            "Profit": profit,
        })

    rows.sort(key=lambda r: r["Date"])
    fieldnames = ["OrderID", "Date", "Region", "Category", "Product",
                  "Quantity", "Sales", "Profit"]
    write_outputs("Hands_On_Activity_Sales_Dashboard", "sales_data",
                  "SALES_DATA", rows, fieldnames)


## --------------------------------------------------------------------------
## Mini Project - InsightRetail (with State + Customer Segment, for a map)
## Columns exactly as named in the brief:
##   Order ID, Date, Region, State, Product, Category, Units, Unit Price,
##   Customer Segment (+ calculated Revenue, Profit)
## State names match the US-states GeoJSON so the choropleth map can join.
## --------------------------------------------------------------------------
def generate_miniproject():
    """Build the Mini-Project dataset (US-state level sales for the choropleth map)."""
    rnd = random.Random(SEED + 4)

    # Region -> list of US states (full names, matching the GeoJSON).
    region_states = {
        "West": ["California", "Washington", "Oregon", "Nevada", "Arizona", "Colorado"],
        "East": ["New York", "Massachusetts", "Pennsylvania", "New Jersey", "Virginia"],
        "Central": ["Illinois", "Ohio", "Michigan", "Missouri", "Minnesota"],
        "South": ["Texas", "Florida", "Georgia", "North Carolina", "Tennessee"],
    }
    region_weights = {"West": 0.32, "East": 0.26, "Central": 0.21, "South": 0.21}

    # category -> (products, base_unit_price, profit_margin)
    catalogue = {
        "Technology": (["Phones", "Computers", "Accessories"], 420, 0.16),
        "Furniture": (["Chairs", "Tables", "Bookcases", "Furnishings"], 260, 0.05),
        "Office Supplies": (["Binders", "Paper", "Storage", "Art"], 22, 0.20),
    }
    cat_weights = {"Technology": 0.40, "Furniture": 0.28, "Office Supplies": 0.32}
    segments = {"Consumer": 0.52, "Corporate": 0.30, "Home Office": 0.18}

    start = date(2024, 1, 1)
    end = date(2024, 12, 31)
    all_days = daterange(start, end)
    season = {1: 0.80, 2: 0.82, 3: 0.95, 4: 1.00, 5: 1.05, 6: 0.95,
              7: 0.92, 8: 1.00, 9: 1.10, 10: 1.18, 11: 1.32, 12: 1.45}

    def day_weight(d):
        trend = 1.0 + (d - start).days / len(all_days) * 0.5
        return trend * season[d.month]

    weights = [day_weight(d) for d in all_days]
    reg_names = list(region_states); reg_w = [region_weights[r] for r in reg_names]
    cat_names = list(cat_weights); cat_w = list(cat_weights.values())
    seg_names = list(segments); seg_w = list(segments.values())

    rows = []
    n_orders = 700
    for i in range(1, n_orders + 1):
        d = rnd.choices(all_days, weights=weights, k=1)[0]
        region = rnd.choices(reg_names, weights=reg_w, k=1)[0]
        state = rnd.choice(region_states[region])
        category = rnd.choices(cat_names, weights=cat_w, k=1)[0]
        products, base_price, margin = catalogue[category]
        product = rnd.choice(products)
        segment = rnd.choices(seg_names, weights=seg_w, k=1)[0]

        unit_price = round(base_price * rnd.uniform(0.6, 1.9), 2)
        units = rnd.randint(1, 12)
        revenue = round(unit_price * units, 2)
        # margin varies; Furniture can dip slightly negative (discount-heavy)
        margin_factor = margin * rnd.uniform(0.2, 1.8) - (0.04 if category == "Furniture" else 0)
        profit = round(revenue * margin_factor, 2)

        rows.append({
            "Order ID": "ORD-%05d" % i,
            "Date": d.isoformat(),
            "Region": region,
            "State": state,
            "Product": product,
            "Category": category,
            "Units": units,
            "Unit Price": unit_price,
            "Customer Segment": segment,
            "Revenue": revenue,
            "Profit": profit,
        })

    rows.sort(key=lambda r: r["Date"])
    fieldnames = ["Order ID", "Date", "Region", "State", "Product", "Category",
                  "Units", "Unit Price", "Customer Segment", "Revenue", "Profit"]
    write_outputs("Mini_Project_InsightRetail_Dashboard", "insightretail_sales",
                  "SALES_DATA", rows, fieldnames)


if __name__ == "__main__":
    print("Generating synthetic sample data (seed=%d)..." % SEED)
    generate_sales()
    generate_customers()
    generate_hr()
    generate_handson()
    generate_miniproject()
    print("Done. All data is synthetic - no personal data included.")
