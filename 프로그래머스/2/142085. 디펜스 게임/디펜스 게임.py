import heapq

def solution(n, k, enemy):    
    life = n
    heap = []
    
    for stage, cur_enemy in enumerate(enemy):
        heapq.heappush(heap, -cur_enemy)
        life -= cur_enemy
        
        if life<0:
            if k>0:
                life += -heapq.heappop(heap)
                k -= 1
            else:
                return stage
    
    return len(enemy)