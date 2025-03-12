x = int(input("Enter the value of X : "))
y = int(input("Enter the value of Y : "))
z = int(input("Enter the value of Z : "))

if x == y and y == z : print("equillateral")
elif x == y or y ==  z or x == z: print('isoceles')
else: print("scalene")