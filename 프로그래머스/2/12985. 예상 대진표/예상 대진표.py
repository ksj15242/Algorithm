def solution(n,a,b):
    roundCount = 0

    while a!=b:
        a, b = (a+1)//2, (b+1)//2
        roundCount += 1
    
    return roundCount