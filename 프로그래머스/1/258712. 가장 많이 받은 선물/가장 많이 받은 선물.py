def solution(friends, gifts):
    n = len(friends)
    
    nameMap = {}
    for i, friend in enumerate(friends):
        nameMap[friend] = i
    
    giftInfo = [[0]*n for _ in range(n)]
    giftIndex = [0]*n
    for gift in gifts:
        give, get = gift.split(" ")
        giveIdx, getIdx = nameMap[give], nameMap[get]
        
        giftInfo[giveIdx][getIdx] += 1
        giftIndex[giveIdx] += 1
        giftIndex[getIdx] -= 1
    
    getNextMonth = [0]*n
    for i in range(n):
        for j in range(i+1, n):
            if giftInfo[i][j]==giftInfo[j][i]:
                if giftIndex[i]>giftIndex[j]:
                    getNextMonth[i] += 1
                elif giftIndex[i]<giftIndex[j]:
                    getNextMonth[j] += 1
                
            elif giftInfo[i][j]>giftInfo[j][i]:
                getNextMonth[i] += 1
            else:
                getNextMonth[j] += 1
    
    return max(getNextMonth)