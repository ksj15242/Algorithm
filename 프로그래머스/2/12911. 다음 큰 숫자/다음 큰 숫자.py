def solution(n):
    neededCount = bin(n).count('1')
    num = n+1
    
    while True:
        numCount = bin(num).count('1')
        
        if neededCount == numCount:
            break
        
        num += 1
        
    return num