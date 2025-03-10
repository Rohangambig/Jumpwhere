def reverseString(string):
    size =  len(string)
    if size % 4 != 0: return string 


    arr = list(string)
    left = 0 ; right = size -1 

    while left < right:
        arr[left] , arr[right] =  arr[right] , arr[left]
        left += 1
        right -= 1
    
    return "".join(arr)

print(reverseString("assignme"))
print(reverseString("jumpwhere"))