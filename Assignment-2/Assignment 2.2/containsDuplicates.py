from collections import Counter

def containsNearbyDuplicate(nums, k):
    size = len(nums)
    rev  = [0] * size
    counter = Counter(nums)
    
    for i in range(size-1,-1,-1):
        rev[i] = nums[i]

    for i in range(size):
        index = size - 1 - rev.index(nums[i])
        if counter[nums[i]] > 1 and index > i and abs(i - index) <= k: return True


    return False 

print(containsNearbyDuplicate([1,2,3,1,2,3],2))