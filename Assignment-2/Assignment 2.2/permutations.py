def permutations(ans,nums,arr,size):
    if len(arr) == size:
        ans.append(arr[:])
        return
    
    for i in range(len(nums)):
        dummy_array = nums[:i] + nums[i+1:]
        arr.append(nums[i])
        permutations(ans,dummy_array,arr,size)
        arr.pop()

def permute(nums):
    ans = []
    size = len(nums)

    permutations(ans,nums,[],size)

    return ans

print(permute([1,2,3]))