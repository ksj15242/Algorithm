def solution(n):
    if n==1:
        return 1
    
    dominator = 1234567
    
    dp = [0]*(n+1)
    dp[0], dp[1], dp[2] = 0, 1, 2
    
    for i in range(3, n+1):
        dp[i] = dp[i-2]+dp[i-1]
    
    return dp[n]%dominator