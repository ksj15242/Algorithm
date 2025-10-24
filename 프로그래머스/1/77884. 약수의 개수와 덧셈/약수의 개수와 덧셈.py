def solution(left, right):
    answer = 0
    
    for n in range(left, right+1):
        sqrt = int(n**0.5)
        
        if sqrt*sqrt==n:
            answer -= n
        else:
            answer += n
    
    return answer