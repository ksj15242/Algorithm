def solution(n):
    answer = 0
    sqrt = int(n**0.5)
    
    for i in range(1, sqrt+1):
        if n%i == 0:
            answer += (i+n//i)
    
    if sqrt*sqrt==n:
        answer -= sqrt
    
    return answer