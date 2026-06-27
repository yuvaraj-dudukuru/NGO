score1 = float(input("Enter score 1: ")) 
score2 = float(input("Enter score 2: ")) 
score3 = float(input("Enter score 3: ")) 
average = (score1 + score2 + score3) / 3 
print(f"Average score: {average}") 



'''Explanation: Each input() returns text, so float() converts it to a decimal number. We sum the 
three and divide by 3. The f-string neatly inserts the result. '''