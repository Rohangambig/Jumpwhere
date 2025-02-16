def subsetCombination(ans,size,index,list,arr):
    if index >  size:
        ans.append(list[:])
        return
    
    list.append(arr[index])
    subsetCombination(ans,size,index+1,list,arr)
    list.pop()
    subsetCombination(ans,size,index+1,list,arr)


def subsets(arr):
    ans = []
    size =  len(arr) - 1

    subsetCombination(ans,size,0,[],arr)
    return ans 

print(subsets([1,2,3]))