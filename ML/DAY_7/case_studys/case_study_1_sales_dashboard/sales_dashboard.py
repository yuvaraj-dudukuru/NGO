# =============================================================================
# CASE STUDY 1 — SALES ANALYSIS DASHBOARD
# =============================================================================
# GOAL:
#   Build a small "manager-friendly" dashboard that combines THREE charts in a
#   single figure:
#       1. A LINE chart  -> shows the revenue trend over time (is it growing?)
#       2. A BAR  chart  -> shows which product earns the most revenue
#       3. A HISTOGRAM   -> shows the distribution of order values (spot outliers)
#
#   Putting these three charts side-by-side lets us tell a complete story at a
#   single glance: "Where are we going, what drives it, and what stands out?"
# =============================================================================


# -----------------------------------------------------------------------------
# STEP 1: Import the libraries we need
# -----------------------------------------------------------------------------
# pandas            -> for storing and organising our data in a table (DataFrame)
# matplotlib.pyplot -> for drawing all of our charts
import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# STEP 2: Create the data
# -----------------------------------------------------------------------------
# A DataFrame is like a spreadsheet: rows = records, columns = fields.
# Each list below becomes one column. All lists MUST be the same length so that
# every row lines up correctly.
sales = pd.DataFrame({
    "Month":      ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],  # the 6 months
    "Revenue":    [120, 150, 130, 200, 240, 300],              # revenue per month
    "Product":    ["A", "B", "A", "C", "B", "C"],              # product sold
    "OrderValue": [400, 650, 380, 1200, 700, 5000]             # value of each order
})

# Quick sanity check: print the table so we can SEE the data before plotting.
print("Sales data:")
print(sales)
print()  # blank line for readability


# -----------------------------------------------------------------------------
# STEP 3: Create the dashboard layout
# -----------------------------------------------------------------------------
# plt.subplots(1, 3) creates ONE row with THREE plotting areas (axes).
#   - fig   = the whole figure (the "canvas" that holds everything)
#   - axes  = a list of 3 small charts: axes[0], axes[1], axes[2]
# figsize=(16, 4) sets the canvas size in inches (wide and short = a dashboard row).
fig, axes = plt.subplots(1, 3, figsize=(16, 4))


# -----------------------------------------------------------------------------
# CHART 1: Line chart of revenue over time  (axes[0])
# -----------------------------------------------------------------------------
# A line chart is ideal for showing a TREND across time (months on the x-axis).
# marker="o" puts a dot on each data point so individual months are easy to read.
axes[0].plot(sales["Month"], sales["Revenue"], marker="o", color="blue")
axes[0].set_title("Revenue Trend")   # title shown above this chart
axes[0].set_xlabel("Month")          # label for the x-axis
axes[0].set_ylabel("Revenue")        # label for the y-axis


# -----------------------------------------------------------------------------
# CHART 2: Bar chart of revenue by product  (axes[1])
# -----------------------------------------------------------------------------
# We first need TOTAL revenue per product. groupby("Product") gathers all rows
# that share the same product, and ["Revenue"].sum() adds their revenue together.
# Result is a small table: index = product name, value = total revenue.
product_rev = sales.groupby("Product")["Revenue"].sum()

# .index  -> the product names (A, B, C)  -> used as the bar labels
# .values -> the total revenue numbers     -> used as the bar heights
axes[1].bar(product_rev.index, product_rev.values, color="green")
axes[1].set_title("Revenue by Product")
axes[1].set_xlabel("Product")
axes[1].set_ylabel("Total Revenue")


# -----------------------------------------------------------------------------
# CHART 3: Histogram of order values  (axes[2])
# -----------------------------------------------------------------------------
# A histogram groups numbers into "bins" (ranges) and counts how many fall in
# each bin. It reveals the SHAPE of the data and makes outliers obvious.
# bins=5 splits the order values into 5 ranges.
# edgecolor="black" draws a border around each bar so the bins are easy to see.
axes[2].hist(sales["OrderValue"], bins=5, color="purple", edgecolor="black")
axes[2].set_title("Order Value Distribution")
axes[2].set_xlabel("Order Value")
axes[2].set_ylabel("Count")


# -----------------------------------------------------------------------------
# STEP 4: Finish and show the dashboard
# -----------------------------------------------------------------------------
# tight_layout() automatically adjusts spacing so titles/labels don't overlap.
plt.tight_layout()

# Save the dashboard to an image file so it can be shared or embedded in reports.
plt.savefig("sales_dashboard.png", dpi=150)

# show() opens a window displaying the figure (use this when running locally).
plt.show()


# -----------------------------------------------------------------------------
# STEP 5: Interpret the results (the part managers actually care about)
# -----------------------------------------------------------------------------
# We print the conclusions so the story is captured in text, not just pictures.
print("INTERPRETATION")
print("- Line chart : Revenue rises steadily from 120 to 300 -> strong growth.")
print("- Bar chart  : Product C contributes the most revenue -> top performer.")
print("- Histogram  : Most orders are small (<1000); one order of 5000 is an outlier.")
print()
print("COMBINED INSIGHT:")
print("  The business is growing, driven largely by Product C, and there is one")
print("  exceptional high-value order worth investigating.")
print()
print("RECOMMENDATION:")
print("  Sustain growth, promote Product C, and follow up with the high-value customer.")
