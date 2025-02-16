from collections import Counter
def singleNumber(nums):
  
    hash = Counter(nums)

    for key,values in hash.items():
        if values == 1:
            return key
        
    return -1

print(singleNumber([2,2,1]))