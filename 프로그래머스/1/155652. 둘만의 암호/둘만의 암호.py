def solution(s, skip, index):
    alphaSet = set(chr(i) for i in range(ord('a'), ord('z')+1))
    alphaSet -= set(skip)
    
    alphaList = sorted(list(alphaSet))
    alphaList.sort()
    
    alphaIdx = {k:v for v, k in enumerate(alphaList)}
    
    n = len(alphaList)
    answer = ''
    for c in s:
        idx = (alphaIdx[c]+index)%n
        answer += alphaList[idx]
    
    return answer