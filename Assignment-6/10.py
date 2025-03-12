salary =  int(input("Enter the salary of a person : "))
year = int(input("Enter the year of experience : "))

amount = salary 
if year > 5:
    amount = amount +  (amount * (5 / 100))

print("salary is : ",amount)