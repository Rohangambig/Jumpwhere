import math 
points = [[3,3],[5,-1],[-2,4]]
k = 2 

arr = []
for nums in points:
    arr.append(math.sqrt(nums[0]*nums[0] + nums[1] * nums[1]))

ans = []
while k:
    k -= 1
    index = arr.index(min(arr))
    ans.append(points[index])
    arr[index] = float('inf')

print(ans)