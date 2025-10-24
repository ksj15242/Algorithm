def solution(babbling):
    babbleList = ("aya", "ye", "woo", "ma")
    
    babbleMap = {}
    for babble in babbleList:
        babbleMap[babble[0]] = (babble, len(babble))
        
    count = 0
    for babble in babbling:
        n = len(babble)
        canSpeak = True
        pastBabble = ""
        
        i = 0
        while i<n:
            firstChar = babble[i]
            if firstChar not in babbleMap:
                canSpeak = False
                break
            
            needBabble, m = babbleMap[firstChar]
            curBabble = babble[i:i+m]
            if curBabble==needBabble and curBabble != pastBabble:
                pastBabble = curBabble
                i += m
            else:
                canSpeak = False
                break
        
        if canSpeak:
            count += 1
        
    return count