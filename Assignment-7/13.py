dict =   {1: 1, 4: 16, 5: 25,2: 4, 3: 9, 5: 25,2: 4, 3: 9}
list = []


for keys,values in dict.items():
    if keys in list: dict.pop(keys)
    else: list.append(keys)

print(dict)