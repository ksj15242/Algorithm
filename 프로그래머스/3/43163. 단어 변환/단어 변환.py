from collections import deque

def possibleWord(curWord, nextWord):
    diffCount = 0
    
    for c, n in zip(curWord, nextWord):
        if c!=n:
            diffCount += 1
        
        if diffCount>1:
            return False
    
    return True

def solution(begin, target, words):
    n = len(words)
    visited = [False]*n
    que = deque([(begin, 0)])
    
    while que:
        curWord, curCount = que.popleft()
        if curWord==target:
            return curCount
        
        for i, nextWord in enumerate(words):    
            if not visited[i] and possibleWord(curWord, nextWord):
                visited[i] = True
                que.append((nextWord, curCount+1))
    
    return 0