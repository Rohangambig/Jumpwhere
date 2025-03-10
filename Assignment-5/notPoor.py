def notPoor(string):

    if "not" in string:
        if "poor" in string:
            index = string.index('not')
            string =  string[:index]
            string += 'poor!'

        else:
            string.remove("not ")
            return string 
    
    elif "good" in string:
        return string.replace('good',"poor")

    return string
print(notPoor("The lyrics is not that poor!"))
print(notPoor("The lyrics is good!"))