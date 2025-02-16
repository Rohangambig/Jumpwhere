def longestMountain(arr):
    res = 0
    n = len(arr)
    i = 1
    
    while i < n-1:

        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            j = i
            count = 1

            while j > 0 and arr[j] > arr[j-1]:
                j -= 1
                count += 1

            while i < n-1 and arr[i] > arr[i+1]:
                i += 1
                count += 1
            
            res = max(res,count)
        else:
            i += 1

    return res

print(longestMountain([2,1,4,7,3,2,5]))