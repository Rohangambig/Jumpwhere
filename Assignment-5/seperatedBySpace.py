def seperatedBySpace(string1,string2):

    return string2[0:2]+string1[2] + " " + string1[0:2] + string2[2]

print(seperatedBySpace("abc","xyz"))