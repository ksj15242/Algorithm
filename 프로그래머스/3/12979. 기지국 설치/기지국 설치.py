def solution(n, stations, w):
    m = len(stations)
    scope = 2*w+1
    count = 0
    
    leftGap = stations[0]-w-1
    if 0<=leftGap:
        count += (leftGap+scope-1)//scope
    
    
    rightGap = n-(stations[-1]+w)
    if rightGap<=n:
        count += (rightGap+scope-1)//scope
    
    for i in range(m-1):
        start = stations[i]+w+1
        end = stations[i+1]-w-1
        
        midGap = end-start+1
        if 0<midGap:
            count += (midGap+scope-1)//scope
        
    return count