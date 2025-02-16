def missingNumber(nums):
    nums.sort()
    i = 1
    size = len(nums)
    ans = []


    def binarySearch(num):
        low , high = 0 , len(nums)-1

        while low <=  high:
            mid = (low + high) // 2
            if nums[mid] == num: return False
            elif nums[mid] > num: high = mid - 1
            else: low = mid + 1
            
        return True

    while i <=  size:
        if binarySearch(i): ans.append(i)
        i += 1
    
    return ans

print(missingNumber([1,3,3,2,6,6,7,8]))