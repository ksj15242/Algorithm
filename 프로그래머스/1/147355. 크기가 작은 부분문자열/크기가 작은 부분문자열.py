def solution(t, p):
    n, m = len(t), len(p)
    
    count = 0
    for i in range(n-m+1):
        if t[i:i+m] <= p:
            count += 1
    
    return count