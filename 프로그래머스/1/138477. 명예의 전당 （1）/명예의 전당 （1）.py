import heapq

def solution(k, score):
    heap = []
    answer = []
    
    for num in score:
        heapq.heappush(heap, num)
        
        if len(heap)>k:
            heapq.heappop(heap)
            
        answer.append(heap[0])
        
    return answer
            
            