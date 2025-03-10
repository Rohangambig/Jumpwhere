def first2last2(string):
    if len(string) < 2: return 'Empty string'
    ans = ""

    ans += string[0:2]
    ans += string[-2::]

    return ans 

print("First 2 and Last2 of the character of a string is : ",first2last2("thisisniceone"))
print("First 2 and Last2 of the character of a string is : ",first2last2("ab"))
print("First 2 and Last2 of the character of a string is : ",first2last2("f"))