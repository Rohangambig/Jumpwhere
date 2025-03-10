def commaSeperated(string):
    arr = list(string.split(','))

    return sorted(list(set(arr)))

print(commaSeperated("banana,apple,orange,banana,grape,apple"))
print(commaSeperated("red,white,black,red,green,black"))