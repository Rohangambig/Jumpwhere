def missingNumber(nums):
    size = len(nums)

    return (size * (size + 1)) // 2 - (sum(nums)) 

print(missingNumber([0,1,3]))