def solution(cards1, cards2, goal):
    canMake = "Yes"
    firstCardIdx, secondCardIdx = 0, 0
    n, m = len(cards1), len(cards2)
    
    for word in goal:
        if firstCardIdx<n and cards1[firstCardIdx]==word:
            firstCardIdx += 1
        elif secondCardIdx<m and cards2[secondCardIdx]==word:
            secondCardIdx += 1
        else:
            canMake = "No"
            break
    
    return canMake