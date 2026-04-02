def solution(name, yearning, photo):
    missScore = {}
    for n, y in zip(name, yearning):
        missScore[n] = y
    
    scoreList = [0]*len(photo)
    for i, people in enumerate(photo):
        for pName in people:
            scoreList[i] += missScore.get(pName, 0)
        
    return scoreList