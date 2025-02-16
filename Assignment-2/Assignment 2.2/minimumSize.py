def minimumSize(arr,target):
    ans = float('inf')
    left =  right  = 0
    size =  len(arr) 
    
    total = 0
    for right in range(size):
        total += arr[right]
        
        while total >= target:
            ans = min(ans,right-left+1)
            total -= arr[left]
            left += 1 
    
    if ans == float('inf') : return 0
    return ans
    
print(minimumSize([1,1,1,1,1,1,1,1],11))