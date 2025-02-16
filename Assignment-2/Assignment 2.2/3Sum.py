def threeSum(nums):
    res = []
    nums.sort()
    size = len(nums)

    for i in range(size):
        
        if i > 0 and nums[i] == nums[i-1]:
            continue

        j = i + 1
        k = size - 1

        while j < k:
            target = nums[i] + nums[j] + nums[k]
            if target > 0:
                k -= 1
            elif target < 0:
                j += 1
            else:
                res.append((nums[i],nums[j],nums[k]))
                j += 1

                while nums[j-1] == nums[j] and j < k:
                    j += 1
        
    return res

print(threeSum([-1,0,1,2,-1,-4]))