def maxSubArray(nums):
    ans = float('-inf')
    left = 0
    right = 0
    total = 0
    size = len(nums)

    while right < size:
        total += nums[right]
        ans = max(ans,total)
        
        while total < 0:
            
            total -= nums[left]
            left += 1
        
        right += 1

    return ans 

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(maxSubArray([5,4,-1,7,8]))
