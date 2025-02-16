def bruteforceMethod(nums):
    ans = []
    size =  len(nums)
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[i] > nums[j]: count += 1
        ans.append(count)
    
    return ans


def efficientAlgorithm(nums):
    counter = {}
    temp =  sorted(nums)

    for i , val in enumerate(temp):
        if val not in counter:
            counter[val] = i 
    
    res = []
    for num in nums:
        res.append(counter[num])
    return res

print(bruteforceMethod([8,1,2,2,3]))
print(efficientAlgorithm([8,1,2,2,3]))