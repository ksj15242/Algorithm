def solution(s):
    answer = [-1]*len(s)
    
    wordMap = {}
    for i, c in enumerate(s):
        if c in wordMap:
            answer[i] = i-wordMap[c]
        
        wordMap[c] = i
        
    return answer