def combination(ans,nums,index,n,arr,k):
    if(len(arr) == k):
        ans.append(arr[:])
        return 
    
    elif index >= n: return 

    arr.append(nums[index])
    combination(ans,nums,index+1,n,arr,k)
    arr.pop()
    combination(ans,nums,index+1,n,arr,k)


def combine(n, k):
    ans = []
    nums = [i+1 for i in range(n) ]
    
    combination(ans,nums,0,n,[],k)
    return ans

print(combine(4,2))