d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}


for keys,values in d2.items():
    if keys in d1: d1[keys] += values 
    else: d1[keys] = values 

print(d1)