def solution(numbers, hand):
    keyPad = ((1,2,3), (4,5,6), (7,8,9),('*',0,'#'))
    n, m = len(keyPad), len(keyPad[0])
    
    keyPadMap = {}
    for i in range(n):
        for j in range(m):
            keyPadMap[keyPad[i][j]] = (i, j)
    
    leftHandPos = keyPadMap['*']
    rightHandPos = keyPadMap['#']
    handOrders = ""
    
    for number in numbers:
        if number in (1, 4, 7):
            handOrders += 'L'
            leftHandPos = keyPadMap[number]
        elif number in (3, 6, 9):
            handOrders += 'R'
            rightHandPos = keyPadMap[number]
        else:
            numberX, numberY = keyPadMap[number]
            leftToNumDist = abs(numberX-leftHandPos[0])+abs(numberY-leftHandPos[1])
            rightToNumDist = abs(numberX-rightHandPos[0])+abs(numberY-rightHandPos[1])
            
            if leftToNumDist<rightToNumDist:
                handOrders += 'L'
                leftHandPos = keyPadMap[number]
            elif leftToNumDist>rightToNumDist:
                handOrders += 'R'
                rightHandPos = keyPadMap[number]
            else:
                if hand=="left":
                    handOrders += 'L'
                    leftHandPos = keyPadMap[number]
                else:
                    handOrders += 'R'
                    rightHandPos = keyPadMap[number]
    
    return handOrders