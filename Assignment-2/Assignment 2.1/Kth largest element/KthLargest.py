def KthLargest(arr,k):
    arr.sort()

    return arr[len(arr)-k]

if __name__ == "__main__":
    arr = [4,2,9,7,5,6,7,1,3]
    k = 4

    print(f"{k} th largest element in an given array {arr} is : ",KthLargest(arr,k))