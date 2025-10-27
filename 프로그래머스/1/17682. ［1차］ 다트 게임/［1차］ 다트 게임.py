def solution(dartResult):
    bonus = {'S':1, 'D':2, 'T':3}
    
    scores = []
    num = ''
    for c in dartResult:
        if c.isdigit():
            num += c
            continue
        
        if c in bonus:
            score = int(num)**(bonus[c])
            scores.append(score)
            num = ''
            continue
        
        if c=='*':
            scores[-1] *= 2
            
            if len(scores)>1:
                scores[-2] *= 2
            
        elif c=='#':
            scores[-1] *= -1
            
    return sum(scores)