import pandas as pd

customers = pd.DataFrame({ 
    "Customer": ["A", "B", "C", "D", "E"], 
    "City": ["Mumbai", "Delhi", "Mumbai", "Pune", "Delhi"], 
    "TotalOrders": [45, 12, 30, 8, 25], 
    "TotalSpent": [90000, 24000, 60000, 16000, 50000] 
}) 
 
# High-value customers: spent more than 40000 
high_value = customers[customers["TotalSpent"] > 40000] 
print("High-value customers:") 
print(high_value) 
 
print("\nCustomers per city:") 
print(customers["City"].value_counts()) 


'''Explanation: We filtered for high-value customers (spent > 40,000) and used value_counts() to 
see the customer distribution across cities. These are exactly the questions a marketing team asks. '''