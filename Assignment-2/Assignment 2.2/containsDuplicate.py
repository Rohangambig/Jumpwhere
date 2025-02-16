from collections import Counter 

def containsDuplicate(nums):
    hash = Counter(nums)

    for k,v in hash.items():
        if v > 1: return True
    return False

print(containsDuplicate([1,2,3,1]))
print(containsDuplicate([1,2,3,4]))