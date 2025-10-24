def solution(s):
    answer = 0
    
    x = ''
    count = 0
    
    for c in s:
        if x=='':
            x = c
            count += 1
            continue
        
        if c==x:
            count += 1
        else:
            count -= 1
        
        if count==0:
            answer += 1
            x = ''
            count = 0
            
    answer += 1 if x else 0
    
    return answer