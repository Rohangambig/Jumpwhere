amount =  int(input("Enter the amount of item : "))
cost  = amount 
if amount > 1000:
    cost = amount - ( amount * (0.1))

print(cost)