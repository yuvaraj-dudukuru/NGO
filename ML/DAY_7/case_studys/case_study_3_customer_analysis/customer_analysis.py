# =============================================================================
# CASE STUDY 3 — CUSTOMER DATASET ANALYSIS
# =============================================================================
# GOAL:
#   Explore a customer dataset (EDA = Exploratory Data Analysis) with THREE
#   charts that each answer a different business question:
#       1. A PIE       chart -> what SHARE of customers comes from each city?
#       2. A BAR       chart -> what is the AVERAGE spend per city?
#       3. A HISTOGRAM       -> how are customer AGES distributed?
#
#   The interesting part is the CONTRAST between charts 1 and 2:
#   the city with the MOST customers is not always the city that SPENDS the most.
#   Finding that kind of contrast is exactly what EDA is for.
# =============================================================================


# -----------------------------------------------------------------------------
# STEP 1: Import the libraries
# -----------------------------------------------------------------------------
import pandas as pd               # for the data table (DataFrame)
import matplotlib.pyplot as plt   # for drawing the charts


# -----------------------------------------------------------------------------
# STEP 2: Create the data
# -----------------------------------------------------------------------------
# Each customer has:
#   - the City they live in
#   - their Age
#   - the total amount they have spent (TotalSpent)
# Note: some cities (e.g. Mumbai, Pune, Delhi) appear more than once because we
# have multiple customers from the same city.
customers = pd.DataFrame({
    "City":       ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Delhi", "Mumbai"],
    "Age":        [25, 34, 28, 45, 31, 52, 29],
    "TotalSpent": [24000, 75000, 16000, 90000, 36000, 10000, 55000]
})

# Print the table to inspect it before plotting.
print("Customer data:")
print(customers)
print()


# -----------------------------------------------------------------------------
# STEP 3: Create the report layout
# -----------------------------------------------------------------------------
# plt.subplots(1, 3) -> one row with THREE charts: axes[0], axes[1], axes[2].
fig, axes = plt.subplots(1, 3, figsize=(16, 4))


# -----------------------------------------------------------------------------
# CHART 1: Pie chart of customer share by city  (axes[0])
# -----------------------------------------------------------------------------
# value_counts() counts how many times each city appears -> number of customers
# per city. A pie chart shows each city's slice as a PERCENTAGE of the whole.
city_counts = customers["City"].value_counts()

# autopct="%1.1f%%" writes the percentage (1 decimal place) on each slice.
# startangle=90 rotates the pie so the first slice starts at the top.
axes[0].pie(city_counts.values, labels=city_counts.index,
            autopct="%1.1f%%", startangle=90)
axes[0].set_title("Customer Share by City")


# -----------------------------------------------------------------------------
# CHART 2: Bar chart of AVERAGE spend by city  (axes[1])
# -----------------------------------------------------------------------------
# groupby("City")["TotalSpent"].mean() gathers all customers in each city and
# computes the AVERAGE amount they spent. This tells us value per customer,
# not just headcount.
city_spend = customers.groupby("City")["TotalSpent"].mean()

axes[1].bar(city_spend.index, city_spend.values, color="orange")
axes[1].set_title("Average Spend by City")
axes[1].set_xlabel("City")
axes[1].set_ylabel("Avg Spend")


# -----------------------------------------------------------------------------
# CHART 3: Histogram of customer ages  (axes[2])
# -----------------------------------------------------------------------------
# A histogram groups ages into 5 bins and counts how many customers fall in each.
# This reveals the typical age range of our customers.
axes[2].hist(customers["Age"], bins=5, color="green", edgecolor="black")
axes[2].set_title("Customer Age Distribution")
axes[2].set_xlabel("Age")
axes[2].set_ylabel("Count")


# -----------------------------------------------------------------------------
# STEP 4: Finish and show the report
# -----------------------------------------------------------------------------
plt.tight_layout()
plt.savefig("customer_analysis.png", dpi=150)
plt.show()


# -----------------------------------------------------------------------------
# STEP 5: Interpret the results
# -----------------------------------------------------------------------------
print("INTERPRETATION")
print("- Pie chart : Mumbai has the largest customer share -> biggest base.")
print("- Bar chart : Average spend is highest in Delhi, even with fewer")
print("              customers -> high-value customers there.")
print("- Histogram : Ages span a wide range; most are late 20s to early 30s.")
print()
print("COMBINED INSIGHT:")
print("  Mumbai brings volume; Delhi brings high spenders.")
print("  Our core customers are young adults.")
print()
print("RECOMMENDATION:")
print("  Grow the customer base in Delhi to capture more high-value spenders,")
print("  and tailor marketing to young adults.")
