def absoluteDifference(nums):
    nums.sort()

    res = []
    i = 0 
    size = len(nums)
    
    difference = float('inf')
    while i < size-1:
        difference = min(difference,abs(nums[i] - nums[i+1]))
        i += 1

    i = 0 
    while i < size-1:
        if abs(nums[i] - nums[i+1]) ==  difference:
            res.append((nums[i],nums[i+1]))
        i += 1
    
    return res

print(absoluteDifference([3,8,-10,23,19,-4,-14,27]))