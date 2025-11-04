def solution(k, tangerine):
    sizeCount = {}
    for tanger in tangerine:
        sizeCount[tanger] = sizeCount.get(tanger, 0)+1
    
    countList = list(sizeCount.values())
    countList.sort(reverse = True)
    
    selected = 0
    typeCount = 0
    for count in countList:
        selected += count
        typeCount += 1
        
        if selected>=k:
            break
            
    return typeCount