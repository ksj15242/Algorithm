def solution(topping):
    toppingTypes = set(topping)
    
    right = {}
    for tp in topping:
        right[tp] = right.get(tp,0)+1
    
    rightTypeCount = len(toppingTypes)
    leftType = set()
    count = 0
    
    for curTopping in topping:
        leftType.add(curTopping)
        
        right[curTopping] -= 1
        if right[curTopping]==0:
            rightTypeCount -= 1
        
        if len(leftType)==rightTypeCount:
            count += 1
        
    return count