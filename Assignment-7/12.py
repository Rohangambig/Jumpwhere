dict =   {1: 1, 4: 16, 5: 25,2: 4, 3: 9}
minimum = float('inf')
maximum = float('-inf')

for keys,values in dict.items():
    if values < minimum: minimum =  values
    if values > maximum: maximum = values 

print("Minimum values in the dictionary is: ",minimum)
print("Maximum values in the dictionary is: ",maximum)