def GenerateParanthesis(arr,left,right,n,string):
    if len(string) == n*2: arr.append(string)

    if left < n: GenerateParanthesis(arr,left+1,right,n,string + '(')
    if right < left:GenerateParanthesis(arr,left,right+1,n,string + ')')

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    arr = []
    GenerateParanthesis(arr,0,0,n,"")
    print(arr)