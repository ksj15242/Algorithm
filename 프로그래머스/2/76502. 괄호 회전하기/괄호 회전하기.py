from collections import deque

def isCorrectString(que):
    bracketMatch = {'[':']', '(':')', '{':'}'}
    stack = []
    
    for c in que:
        if c in bracketMatch:
            stack.append(c)
            continue
        
        if not stack:
            return False
        
        if bracketMatch[stack[-1]]!=c:
            return False
        
        stack.pop()
    
    return True if not stack else False

def solution(s):
    answer = 0
    n = len(s)
    
    rotCount = n
    que = deque(s)
    
    while rotCount>0:
        if isCorrectString(que):
            answer += 1
        
        que.append(que.popleft())
        rotCount -= 1
    
    return answer