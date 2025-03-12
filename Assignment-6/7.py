def greater30(arr):
    count = 0 
    for num in arr:
        if num > 30: count += 1

    return count 

print(greater30([34,13,1,4,2,4,5,4354,6,4,3,3,55,3,233]))