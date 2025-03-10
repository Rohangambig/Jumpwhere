def convertUpperCase(string):
    count = 0
    i = 0

    for char in string:
        i += 1
        if ord(char) < 96: count += 1
        if count == 2: return string.upper()
        if i == 4: return string

    return string 
print(convertUpperCase("Rohan"))
print(convertUpperCase("JumPWhere"))