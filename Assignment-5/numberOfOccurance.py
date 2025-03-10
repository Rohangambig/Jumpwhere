from collections import Counter 

def occurance1(string):
    dict = Counter(string)
    return dict 

def occurance2(string):
    dict = {}
    for char in string:
        if char in dict: dict[char] += 1
        else: dict[char] = 1
    
    return dict

print("Frequency of the string is : ",occurance1('google.com'))
print("Frequency of the string is : ",occurance2('google.com'))