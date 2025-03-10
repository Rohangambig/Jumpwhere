import math

def armstrongNumber ( m):
    count = math.log10(m) +1
    num = int(count)
    
    n = m
    ans = 0
    while n!= 0:
        rem = n % 10
        n = n // 10
        ans = ans + ( pow(rem,num) )
    
    return ans == m

print(armstrongNumber(153))
print(armstrongNumber(15321))