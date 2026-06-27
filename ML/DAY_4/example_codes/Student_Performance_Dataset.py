import pandas as pd 
students = pd.DataFrame({ 
"Name": ["Asha", "Ravi", "Imran", "Divya", "Karan"], 
"Math": [85, 60, 92, 45, 78], 
"Science": [90, 65, 88, 50, 80], 
"English": [82, 70, 95, 55, 76] 
}) 
# Create a Total and Average column (vectorized, from Day 3) 
students["Total"] = students["Math"] + students["Science"] + students["English"] 
students["Average"] = students["Total"] / 3 
print(students) 
print("\nClass average:", students["Average"].mean()) 
print("\nTop scorer:") 
print(students.sort_values("Total", ascending=False).head(1)) 


'''Explanation: We added new columns by doing vectorized arithmetic on existing columns, computed 
the class average, and used sort_values(...).head(1) to find the top scorer (Imran). Notice 
how Day 3's vectorization carries straight into Pandas. '''