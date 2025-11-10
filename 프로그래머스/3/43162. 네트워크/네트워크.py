from collections import deque

def getConnectionMatrix(computers):
    n = len(computers)
    connections = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i!=j and computers[i][j]==1:
                connections[i].append(j)
    
    return connections

def bfs(i, connections, visited):
    que = deque([i])
    visited[i] = True
    
    while que:
        
        curNode = que.popleft()
        
        for nextNode in connections[curNode]:
            if not visited[nextNode]:
                visited[nextNode] = True
                que.append(nextNode)

def solution(n, computers):
    n = len(computers)
    
    connections = getConnectionMatrix(computers)    
    visited = [False]*n
    
    networkCount = 0
    for i in range(n):
        if not visited[i]:
            bfs(i, connections, visited)
            networkCount += 1
    
    return networkCount