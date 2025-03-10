def changedTo(string):
    list  = []


    for i in range(len(string)):
        if string[i] in list:
            return string[:i] + '$' + string[i+1:]
            
        else:
            list.append(string[i])
        
    return 1

print(changedTo('restart'))
print(changedTo('jumpwhere'))