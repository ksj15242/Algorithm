def solution(m, n, puddles):
    dominator = 1000000007
    maps = [[0]*(m+1) for _ in range(n+1)]
    maps[1][1] = 1
    
    for y, x in puddles:
        maps[x][y] = -1
        
    for x in range(1, n+1):
        for y in range(1, m+1):
            if (x==1 and y==1) or maps[x][y]==-1:
                continue
            
            if maps[x-1][y]!=-1:
                maps[x][y] += maps[x-1][y]
            
            if maps[x][y-1]!=-1:
                maps[x][y] += maps[x][y-1]
            
            maps[x][y] %= dominator
    
    return maps[n][m]%dominator