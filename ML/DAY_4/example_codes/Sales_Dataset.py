import pandas as pd

sales = pd.DataFrame({
    "Product": ["Laptop", "Phone", "Tablet", "Phone", "Laptop"], 
    "Units": [5, 20, 8, 15, 3], 
    "Price": [60000, 30000, 20000, 30000, 60000] 
}) 
sales["Revenue"] = sales["Units"] * sales["Price"] 
 
print(sales) 
print("\nTotal revenue:", sales["Revenue"].sum()) 
print("\nUnits sold per product:") 
print(sales.groupby("Product")["Units"].sum())



'''Explanation: We computed revenue per row, totaled it, and introduced groupby() — which 
groups rows by a category (Product) and aggregates (sums) within each group. groupby is one of 
the most powerful analysis tools; you will study it in depth later, but here it instantly shows that 
Phones sold the most units (35). '''