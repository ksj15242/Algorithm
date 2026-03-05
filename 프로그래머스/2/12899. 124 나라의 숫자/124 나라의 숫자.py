def solution(n):
    answer = ''

    while n:
        r = n%3
        
        if r==0:
            answer += '4'
            n = n//3-1
        elif r==1:
            answer += '1'
            n //= 3
        elif r==2:
            answer += '2'
            n //= 3
    
    return answer[::-1]