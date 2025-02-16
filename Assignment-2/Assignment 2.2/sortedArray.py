def sortedSquares(nums):
    ans = [] 

    for num in nums:
        ans.append(num ** 2)

    return sorted(ans)

def efficientMethod(nums):
    
    n = len(nums)
    left = 0
    right = n - 1
    res = [0] * n
    i = n-1

    while left <=  right:
        if nums[left] * nums[left] >= nums[right] * nums[right]:
            res[i] = nums[left] * nums[left]
            i -= 1
            left += 1
        if nums[left] * nums[left] <= nums[right] * nums[right]:
            res[i] = nums[right] * nums[right]
            i -= 1
            right -= 1
        
    return res

print(sortedSquares([-4,-1,0,3,10]))
print(efficientMethod([-4,-1,0,3,10]))