import math

def isPrime(num):
    if num <= 3: return True
    if num % 2 == 0 or num  % 3 == 0: return False

    for i in range(5,int(math.sqrt(num))+1):
        if num % i == 0: return False 
    
    return True

list1 = [];list2 = [];list3 = []

for i in range(1,101):
    if i & 1 == 1: list1.append(i)
    else: list2.append(i)
    if isPrime(i): list3.append(i)


print("Even number list : ",list2)
print("\nOdd number list : ",list1)
print("\nPrime number list : ",list3)