import heapq
from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

counter = Counter(nums)
heap = [(-count,num) for num , count in counter.items()]

heapq.heapify(heap)
ans = []
while k:
    k -=1 
    ans.append(heapq.heappop(heap)[1])

print("Top K Frequent Elements : ",ans)