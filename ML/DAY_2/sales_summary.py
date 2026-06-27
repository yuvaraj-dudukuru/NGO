# ShopSmart - Weekly Sales Summary
# A small program that takes one week of daily sales and prints a quick summary.

# Store the week's daily sales (Monday to Sunday) in a list
daily_sales = [3200, 4500, 2800, 5100, 6200, 7400, 5600]

# A matching list of weekday names (used for the stretch goals)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Calculate the key summary figures
total = sum(daily_sales)                 # total sales for the whole week
average = total / len(daily_sales)       # average sales per day
highest = max(daily_sales)               # best day's sales
lowest = min(daily_sales)                # worst day's sales
difference = highest - lowest            # gap between best and worst day

# Print the core results (using a clear f-string for the average)
print("Total weekly sales:", total)
print(f"Average daily sales: {average}")
print("Highest sales day:", highest)
print("Lowest sales day:", lowest)
print("Difference between best and worst day:", difference)

# ---------------- Stretch goals ----------------

# 1) Round the average to two decimals
print(f"Average daily sales (rounded): {round(average, 2)}")

# 2) Identify which weekday had the highest (and lowest) sales
best_day = days[daily_sales.index(highest)]
worst_day = days[daily_sales.index(lowest)]
print(f"Best day: {best_day} ({highest})")
print(f"Worst day: {worst_day} ({lowest})")

# 3) Count how many days had above-average sales
above_average = sum(1 for sale in daily_sales if sale > average)
print(f"Days with above-average sales: {above_average}")
