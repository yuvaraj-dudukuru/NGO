budget = 10000 
expenses = [2500, 1800, 3200, 1500]     # list of expenses 
total_spent = sum(expenses) 
remaining = budget - total_spent 

print("Total spent:", total_spent) 
print("Remaining budget:", remaining) 

'''Explanation: We total the expenses with sum(), then subtract from the budget to find what is left. 
This mirrors real expense dashboards.'''