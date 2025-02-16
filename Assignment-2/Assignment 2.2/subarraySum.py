def findSum(nums,i,k,sum,count):
    if i < 0: return count
    if sum > k: return 0
    elif  sum == k: count += 1

    left = findSum(nums,i-1,k,sum+nums[i],count)
    right = findSum(nums,i-1,k,sum,count)

    return left + right

def subArray(arr,k):
    size = len(arr)-1
    nums.sort()

    print("number of subarray : ", findSum(arr,size,k,0,0))

if __name__ == "__main__":
    nums = [1,1,1]
    k = 2

    subArray(nums,k)