def solution(n, words):
    lastAlpha = words[0][-1]
    seen = {words[0]}
    
    failedNum, failedTurn = 0, 0
    for i, word in enumerate(words[1:]):
        
        if lastAlpha!=word[0] or word in seen:
            return [(i+1)%n+1, (i+1)//n+1]
            
        lastAlpha = word[-1]
        seen.add(word)

    return [0,0]