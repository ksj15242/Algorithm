def solution(mats, park):
    height = len(park)
    width = len(park[0])
    
    dp = [[0]*(width+1) for _ in range(height+1)]
    
    maxMatSize = 0
    for x in range(1, height+1):
        for y in range(1, width+1):
            if park[x-1][y-1] == "-1":
                dp[x][y] = min(dp[x-1][y], dp[x][y-1], dp[x-1][y-1]) + 1
            
            maxMatSize = max(maxMatSize, dp[x][y])
        
    mats.sort(reverse=True)
    for mat in mats:
        if mat<=maxMatSize:
            return mat
            
    return -1