import heapq

arr = [3,2,3,1,2,4,5,5,6]

k = 4 

nums =[-num for num in arr]
heapq.heapify(nums)

while k > 1:
    k-=1
    heapq.heappop(nums)

print(-heapq.heappop(nums))