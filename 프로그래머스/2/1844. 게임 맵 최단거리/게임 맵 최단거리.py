from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    mv = ((1,0), (-1,0), (0,1), (0,-1))
    visited = [[False]*m for _ in range(n)]
    que = deque([(0,0,1)])
    visited[0][0] = True
    
    answer = -1
    while que:
        curX, curY, curDist = que.popleft()
    
        if curX==n-1 and curY==m-1:
            answer = curDist
            break
    
        for mx, my in mv:
            nextX, nextY = curX+mx, curY+my
            
            if not (0<=nextX<n and 0<=nextY<m):
                continue
            
            if not visited[nextX][nextY] and maps[nextX][nextY]==1:
                visited[nextX][nextY] = True
                que.append((nextX, nextY, curDist+1))
    
    return answer