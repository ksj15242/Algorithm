def solution(n):
    count = 0
    s, e = 1, 1
    sumNum = 1
    
    while s<=n:
        if sumNum==n:
            count += 1
            e += 1
            sumNum += e
        elif sumNum<n:
            e += 1
            sumNum += e
        else:
            sumNum -= s
            s += 1
            
    return count