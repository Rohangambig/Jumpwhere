dict = {'a': 300, 'b': 200, 'd':400,'c':500,'e':100,'f':800}

max1 = max2 =  max3 = float('-inf')

for keys,values in dict.items():
    if dict[keys]  > max1:
        max3 = max2 
        max2 = max1 
        max1 =  dict[keys] 
    
    elif dict[keys]  > max2:
        max3 = max2
        max2 = dict[keys] 
    
    elif  dict[keys] > max3:  max3 =  dict[keys] 

print("Top maximum values in the dictionary are : ",max1,max2,max3)