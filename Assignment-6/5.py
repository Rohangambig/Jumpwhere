def sumCalculation(num):
    sum = ( (num) * (num+1) ) / 2
    avg = sum / num 

    return {sum,avg}

print(sumCalculation(6))
print(sumCalculation(50))