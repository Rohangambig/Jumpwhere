def checkEmpty(arr):

    for dict in arr:
        if dict: return False
    
    return True 

print(checkEmpty([{},{},{}]))
print(checkEmpty([{1,2},{},{}]))  