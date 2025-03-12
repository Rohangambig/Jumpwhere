arr = list(map(int,input().split()))
item = int(input("Enter the item : "))

size = len(arr)
index = -1
for i in range(size):
    if arr[i] == item:
        index = i; break 

arr.pop(index)
print(arr)