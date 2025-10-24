def solution(a, b, n):
    
    emptyBottle = n
    newBottle = 0
    while emptyBottle>=a:
    
        bundle = emptyBottle//a
        giveBottle = bundle*a
        getBottle = bundle*b
        
        emptyBottle -= giveBottle
        emptyBottle += getBottle
            
        newBottle += getBottle

    return newBottle