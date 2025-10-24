def solution(k, m, score):
    answer = 0
    
    n = len(score)
    score.sort(reverse = True)
    
    for i in range(n//m):
        idx = m*i+(m-1)
        answer += score[idx]*m
    
    return answer