marks = [85, 90, 78, 92, 88]       # a list of marks 
total = sum(marks)                 # sum() adds all items 
average = total / len(marks)       # divide by the count of items 
highest = max(marks)               # max() finds the largest 
lowest = min(marks)                # min() finds the smallest 
print("Total:", total) 
print("Average:", average) 
print("Highest:", highest) 
print("Lowest:", lowest) 



'''Line-by-line: 
• marks = [...] creates a list of five marks. 
• sum(marks) adds them: 85+90+78+92+88 = 433. 
• len(marks) is the number of marks (5); total / len(marks) gives the average 86.6. 
• max() and min() return the largest and smallest values. '''