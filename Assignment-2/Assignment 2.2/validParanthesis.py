def isValid(s):
    dictionary = { 
        
        ')' : '(',
        ']' : '[',
        '}' :'{'
    }

    stack = []
    for char in s:
        if char not in dictionary:
            stack.append(char)
        else:
            if len(stack) == 0 or stack[-1] != dictionary[char]: return False
            stack.pop()
        
    return len(stack) == 0

print(isValid("{}"))