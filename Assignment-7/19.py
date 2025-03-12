list =[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
ans = []

for nums in list: 
    if nums not in ans: ans.append(nums)
    
print(ans)