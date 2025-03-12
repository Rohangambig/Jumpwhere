def pattern(n):

    for i in range(n):
        for j in range(i+1):
            print(i+1,end="")
        print()
    

pattern(5)
pattern(9)