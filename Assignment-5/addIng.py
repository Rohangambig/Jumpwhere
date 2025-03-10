def addIng(string):

    right =  len(string) - 1
    dummyString = "ing"

    for i in range(len(dummyString)-1,-1,-1):
        if dummyString[i] == string[right]:  right -= 1
        else : return string + 'ing'
    
    return string + 'ly'

print("Add ing or ly at the end of the string : ",addIng("abc"))
print("Add ing or ly at the end of the string : ",addIng("string"))