def makeLowercase(pastId):
    return pastId.lower()

def removedNotAllowed(pastId):
    newId = ""
    allowedChar = ('-', '_', '.')
    
    for c in pastId:
        if c.isalpha() or c.isdigit() or c in allowedChar:
            newId += c
        
    return newId

def replaceContinuousPeriodToOne(pastId):
    newId = ""
    continuous = False
    
    for c in pastId:
        if c=='.':
            if not continuous:
                newId += c
                continuous = True
        else:
            newId += c
            continuous = False

    return newId

def removeFirstAndEndPeriod(pastId):
    s, e = 0, len(pastId)
    
    if pastId[0]=='.':
        s += 1
    
    if pastId[-1]=='.':
        e -= 1
    
    return pastId[s:e]

def addNewIfBlank(pastId):
    if pastId=="":
        return "a"
    
    return pastId

def sliceToMaxLength(pastId):
    maxLength = 16
    
    newId = pastId[:maxLength-1]
    if newId[-1]=='.':
        return newId[:-1]

    return newId

def repeatToMakeMinLength(pastId):
    minLength = 3
    idLength = len(pastId)
    
    if idLength>=minLength:
        return pastId
    
    return pastId+pastId[-1]*(minLength-idLength)

def solution(new_id):
    step1 = makeLowercase(new_id)
    step2 = removedNotAllowed(step1)
    step3 = replaceContinuousPeriodToOne(step2)
    step4 = removeFirstAndEndPeriod(step3)
    step5 = addNewIfBlank(step4)
    step6 = sliceToMaxLength(step5)
    step7 = repeatToMakeMinLength(step6)
    
    return step7
