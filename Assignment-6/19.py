list = [1,2,4,2.4,2.4,1,1.32,3.2,"rohan","ambig","qw","g","zx"]
list_int = []
list_float = []
list_string = []

for i in range(len(list)):
    if type(list[i]) ==  int:
        list_int.append(list[i])
    
    elif type(list[i]) ==  float:
        list_float.append(list[i])
    
    elif type(list[i]) ==  str:
        list_string.append(list[i])

print(list_int)
print(list_float)
print(list_string)