def Main(arr,target):
    first = last = -1

    i = 0
    j = len(arr)-1 
    while i < len(arr) or j >= 0:
        if i < len(arr) and arr[i] ==  target: first = i ; i = len(arr) 
        if j >= 0 and arr[j] == target: last = j ;  j = -1 

        i += 1;j -= 1
    
    return [first,last]


if __name__ == "__main__":
    arr = [2,4,5,5,5,5,5,7,9,9]
    target = 5

    print("output : ",Main(arr,target))