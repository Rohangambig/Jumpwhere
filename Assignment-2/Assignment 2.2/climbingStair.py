def numberOfCombination(n,dp):
    if n == 1 or n == 0: return 1 
    elif dp[n] != -1: return dp[n]
    elif n < 0: return 0

    else: 
        dp[n] =  numberOfCombination(n-1,dp) + numberOfCombination(n-2,dp)
        return dp[n]

def climbStairs( n) :
    dp = [-1 for _ in range(n+1) ]
    return numberOfCombination(n,dp)

print(climbStairs(5))