def removeIndex(string,index):
    ans = ""
    for i in range(len(string)):
        if  i !=  index: 
            ans +=  string[i] 
    
    return ans

print(removeIndex("jumpwhere",4))
print(removeIndex("Rohan G Ambig",10))