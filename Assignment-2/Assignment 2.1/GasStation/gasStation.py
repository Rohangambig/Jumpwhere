def completeCircle(gas,cost):
    size = len(gas)
    tank = 0

    for i in range(size):
        for j in range(size):

            tank += gas [ (i+j) % size]
            tank -= cost [ (i+j) % size]
            if tank < 0: tank = 0 ; break 
            if j == size-1: return i 
    return -1

def anotherSolution(gas,cost):
    size = len(gas)
    tank = 0
    maxLength = 0

    for i in range(size * 2):
        tank += gas[i % size] - cost[i % size]
        if tank >= 0: maxLength += 1
        else: maxLength = 0

        tank = max(tank,0)
    
    if maxLength >= size: return (size* 2) - maxLength
    return -1

if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    print(completeCircle(gas,cost))
    print(anotherSolution(gas,cost))