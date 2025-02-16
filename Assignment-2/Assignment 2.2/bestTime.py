def maxProfit(prices):
    profit = 0
    left = 0
    right = 1

    while right < len(prices):
        if prices[left] > prices[right]:
            left = right
        
        if profit < prices[right] - prices[left]:
            profit = prices[right] - prices[left]

        right += 1
    
    return profit

print(maxProfit([7,1,5,3,6,4]))