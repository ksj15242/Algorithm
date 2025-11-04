def solution(s):
    answer = ""
    wordStart = True
    
    for c in s:
        if c.isdigit():
            wordStart = False
            answer += c
        elif c==' ':
            wordStart = True
            answer += c
        else:
            answer += c.upper() if wordStart else c.lower()
            wordStart = False
            
    return answer