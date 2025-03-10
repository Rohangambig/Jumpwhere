def swapCommaDot(string):
    left = 0
    right =  len(string)-1

    print(string)
    while left < right:
        if string[left] == ',' and string[right] == '.':
            string[left], string[right] = string[right],string[left]
            left += 1
            right -= 1
        
        if string[left] != ',':
            left += 1

        if string[right] != '.': right -= 1

    return "".join(string)

print(swapCommaDot("32,054.23"))