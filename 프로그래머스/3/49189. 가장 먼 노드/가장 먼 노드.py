from collections import deque

def bfs(n, table):
    visited = [False]*(n+1)
    dists = [0]*(n+1)
    
    que = deque([1])
    visited[1] = True
    
    while que:
        cur = que.popleft()
        
        for nxt in table[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dists[nxt] = dists[cur]+1
                que.append(nxt)

    return dists

def solution(n, edge):
    table = [[] for _ in range(n+1)]
    for a, b in edge:
        table[a].append(b)
        table[b].append(a)
        
    dists = bfs(n, table)
    max_dist = max(dists)
    
    return dists.count(max_dist)