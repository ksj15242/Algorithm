from collections import deque

def bfs(n, s, graph):
    dists = [-1]*(n+1)
    que = deque([s])
    
    dists[s] = 0
    
    while que:
        cur = que.popleft()
        
        for nxt in graph[cur]:
            if dists[nxt]==-1:
                dists[nxt] = dists[cur]+1
                que.append(nxt)
    
    return dists
    
def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n+1)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
        
    dists = bfs(n, destination, graph)
    
    answer = []
    for source in sources:
        answer.append(dists[source])
    
    return answer