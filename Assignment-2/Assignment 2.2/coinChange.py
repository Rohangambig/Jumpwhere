def allPossibility(coins,amount,i,dp):
    if amount == 0: return 0
    elif i < 0 or amount < 0: return float('inf')
    elif dp[amount][i] != -1: return dp[amount][i]

    left = 1 + allPossibility(coins,amount - coins[i],i,dp)
    right =  allPossibility(coins,amount,i-1,dp)

    dp[amount][i] =  min(left,right)
    return dp[amount][i]

def coinChange(coins, amount) :
    size = len(coins) - 1
    dp = [ [-1] * (size + 1) for _ in range(amount+1) ]
    ans =  allPossibility(coins,amount,size,dp)
    if ans == float('inf'): return -1
    return ans
    
print(coinChange([1,2,5]),11)