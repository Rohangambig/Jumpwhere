def removeDuplicate(string):
    ans = ""

    for char in string:
        if char != ' ' and char not in ans:
            ans += char 
        
        if char == ' ': ans +=  char
    return ans
    

print(removeDuplicate("Rohan g ambig"))