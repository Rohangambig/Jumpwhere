class NumArray:
    def __init__(self,nums):
        self.numArray = nums 
    
    def sumRange(self,left,right):
        return sum(self.numArray[left:right+1])

N = None
ans = []
operation = ["NumArray", "sumRange", "sumRange", "sumRange"]
values =  [[[1, 2, 3, 4, 5]], [0, 2], [1, 3], [2, 4]]
for i in range(len(operation)):
    if operation[i] == "NumArray":
        N = NumArray(values[i])
        ans.append(None)
    else:
        ans.append(N.sumRange(values[i][0],values[i][1]))