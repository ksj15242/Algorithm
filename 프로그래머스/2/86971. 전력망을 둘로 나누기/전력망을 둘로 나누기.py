from collections import deque

def bfs(start_node, cut_edge, graph, n):
    que = deque([start_node])
    visited = [False]*(n+1)
    
    visited[start_node] = True
    count = 1
    
    while que:
        cur_node = que.popleft()
        
        for next_node in graph[cur_node]:
            if (cur_node, next_node)==cut_edge:
                continue
            
            if not visited[next_node]:
                visited[next_node] = True
                que.append(next_node)
                count += 1
    
    return count

def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    min_diff = n
    for a, b in wires:
        count = bfs(a, (a, b), graph, n)
        min_diff = min(min_diff, abs(n-count*2))
    
    return min_diff