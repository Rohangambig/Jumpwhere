def timeRequiredToBuy(tickets, k):
    second = 0
    i = 0

    while tickets[k] >  0:
        if tickets[i] > 0:
            tickets[i] -= 1
            second += 1

        i = ( i + 1) % len(tickets)
        

    return second

print(timeRequiredToBuy([2,3,2],2))