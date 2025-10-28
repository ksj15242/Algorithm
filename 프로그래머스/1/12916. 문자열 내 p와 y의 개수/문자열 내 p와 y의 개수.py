def solution(s):
    s = s.lower()
    
    pCount = 0
    yCount = 0
    
    for c in s:
        if c=='p':
            pCount += 1
        elif c=='y':
            yCount += 1
    
    return pCount==yCount