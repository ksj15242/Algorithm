def solution(n):
    arr = []
    
    while n!=0:    
        arr.append(n%3)
        n //= 3
    
    answer = 0
    i = 0
    while arr:
        answer += arr.pop()*(3**i)
        i += 1
        
    return answer