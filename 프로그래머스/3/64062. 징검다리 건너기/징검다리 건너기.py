import heapq
from collections import deque

def solution(stones, k):
    n = len(stones)
    
    heap = []
    que = deque()
    out_mark = [False]*n
    
    init_max = 0
    for i in range(k):
        heapq.heappush(heap, (-stones[i],i))
        que.append(i)        
        init_max = max(init_max, stones[i])
    
    answer = init_max
    for i in range(k, n, 1):
        out_mark[que.popleft()] = True
        que.append(i)
        heapq.heappush(heap, (-stones[i],i))
        
        while heap and out_mark[heap[0][1]]:
            heapq.heappop(heap)

        answer = min(answer, -heap[0][0])

    return answer