
def countBits(n):
    ans = []
    dp = [-1 for _ in range(n+1) ]

    for i in range(n+1):
        count = 0
        m = i

        while m != 0:
            if dp[m] != -1: count += dp[m]; break
            if m % 2 == 1:count += 1
            m = m // 2

        dp[i] = count
        ans.append(count)
    
    return ans

print(countBits(3))