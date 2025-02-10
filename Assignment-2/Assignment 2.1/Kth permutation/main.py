def permutation(string,substring,k,count):
    if len(string) == 0: 
        count += 1
        if count == k-1: return substring 
        return None
    
    else:
        for i in range(len(string)):
            str = string[:i] + string[i+1:]
            result = permutation(str,substring + string[i],k,count)
            if result: return result 
    
    return None


def kthPermutation(n,k):
    numbers = "123456789"
    string =  numbers[:n]

    return permutation(string,"",k,0)


if __name__ == "__main__":
    n = int(input("Enter the size : "))
    k = int(input("Enter the index : "))

    print(kthPermutation(n,k))