def solution(n):
    sqrt = int(n**0.5)
    
    return (sqrt+1)**2 if n==sqrt*sqrt else -1