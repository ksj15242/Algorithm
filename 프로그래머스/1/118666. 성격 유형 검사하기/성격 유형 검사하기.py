def solution(survey, choices):
    choicePoint = {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    mbtiTypes = ('R', 'T', 'C', 'F', 'J', 'M', 'A', 'N')

    midIdx = 4
    userPoint = { mt:0 for mt in mbtiTypes}
    
    for types, choice in zip(survey, choices):
        typeA, typeB = types
        
        if choice<midIdx:
            userPoint[typeA] += choicePoint[choice]
        elif choice>midIdx:
            userPoint[typeB] += choicePoint[choice]
    
    userMbtiType = ""
    for i in range(0, len(mbtiTypes), 2):
        typeA, typeB = mbtiTypes[i], mbtiTypes[i+1]
        
        if userPoint[typeA]>=userPoint[typeB]:
            userMbtiType += typeA
        else:
            userMbtiType += typeB
            
    return userMbtiType