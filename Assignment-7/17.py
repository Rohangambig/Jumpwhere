dict1 =  {'key1': 1, 'key2': 3, 'key3': 2}
dict2 = {'key1': 1, 'key2': 2}

ans = {}

for keys,values in dict1.items():
    if keys in dict2 and values == dict2[keys]: ans[keys] = values 

print(ans)