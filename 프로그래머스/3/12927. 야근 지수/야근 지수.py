import heapq

def solution(n, works):
    maxHeap = [-w for w in works]
    heapq.heapify(maxHeap)
        
    for _ in range(n):
        if maxHeap[0]==0:
            break
        
        work = heapq.heappop(maxHeap)
        heapq.heappush(maxHeap, work+1)
        
    return sum(w*w for w in maxHeap)