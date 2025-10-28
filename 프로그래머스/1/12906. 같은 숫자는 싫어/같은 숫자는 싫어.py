def solution(arr):
    answer = []
    past = -1
    
    for n in arr:
        if n!=past:
            answer.append(n)
            past = n
    
    return answer