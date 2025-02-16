def twoSum(nums,target):
    store = { }

    for  index, val in enumerate(nums): 
        value = target - val

        if value in store:
            return [store[value],index]
        
        store[value] = index
    
    return None

print(twoSum([2,7,11,15],9))