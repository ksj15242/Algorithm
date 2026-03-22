from collections import deque

def applicant_positions(places):
    applicants = []
    
    for i in range(len(places)):
        for j in range(len(places[0])):
            if places[i][j]=='P':
                applicants.append((i,j))
    
    return applicants

def bfs(x, y, place):
    n, m = len(place), len(place[0])
    mv = ((0,1),(0,-1),(1,0),(-1,0))
    visited = [[False]*m for _ in range(n)]
    
    que = deque([(x,y,0)])
    visited[x][y] = True
    
    while que:
        cx, cy, d = que.popleft()
        
        if d>=2:
            continue
        
        for dx, dy in mv:
            nx, ny = cx+dx, cy+dy
            
            if not (0<=nx<n and 0<=ny<m):
                continue
            
            if visited[nx][ny] or place[nx][ny]=='X':
                continue
                
            if place[nx][ny]=='P':
                return 0
            
            visited[nx][ny] = True
            que.append((nx, ny, d+1))
    
    return 1

def solution(places):
    answer = []
    
    for place in places:
        result = 1
        
        for x, y in applicant_positions(place):
            if bfs(x,y,place)==0:
                result = 0
                break
                
        answer.append(result)
                
    return answer