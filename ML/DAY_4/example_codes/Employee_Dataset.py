import pandas as pd

employees = pd.DataFrame({ 
    "Name": ["Rajesh", "Priya", "Aman", "Sneha", "Karan"], 
    "Department": ["IT", "HR", "IT", "Finance", "IT"], 
    "Salary": [50000, 75000, 40000, 90000, 60000] 
}) 
 
print("Average salary by department:") 
print(employees.groupby("Department")["Salary"].mean()) 
print("\nHighest-paid employee:") 
print(employees.sort_values("Salary", ascending=False).head(1)) 


'''Explanation: groupby("Department")["Salary"].mean() computes the average salary within 
each department, revealing that IT has the lowest average. Sorting finds the single highest-paid 
employee.'''