from collections import deque

def solution(priorities, location):
    que = deque([(i, p) for i, p in enumerate(priorities)])
    priorities.sort(reverse = True)
    
    popCount = 0
    
    while que:
        idx, priority = que[0]
        needPriority = priorities[popCount]
        
        if priority>=needPriority:
            if idx==location:
                break
            
            popCount += 1
            que.popleft()
        else:
            que.append(que.popleft())
    
    return popCount+1