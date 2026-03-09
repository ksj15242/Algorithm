import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for a,b,c in road:
        graph[a].append((c,b))
        graph[b].append((c,a))
    
    dists = [float('inf')]*(N+1)
    dists[1] = 0
    
    heap = [(0,1)]
    
    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        if cur_dist > dists[cur_node]:
            continue
        
        for nxt_dist, nxt_node in graph[cur_node]:
            sum_dist = cur_dist+nxt_dist
            
            if dists[nxt_node]>sum_dist:
                dists[nxt_node] = sum_dist
                heapq.heappush(heap, (sum_dist, nxt_node))

    return sum(1 for dist in dists if dist <= K)