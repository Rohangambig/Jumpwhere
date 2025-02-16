# square the given number
square = lambda x : x ** 2
print(square(4))

# sort the given array 
data = [(1,2),[3,2],[0,1]]
sortedArray = sorted(data,key = lambda arr : arr[1])
print(sortedArray)

# filter the value
arr  = [1,2,3,4,5,6]
filteredArray = list(filter(lambda x:  x % 2 == 0 ,arr))
print(filteredArray)