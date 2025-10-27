def solution(d, budget):
    d.sort()
    
    usedBudget = 0
    count = 0
    
    for n in d:    
        if budget<usedBudget+n:
            break
        
        usedBudget += n
        count += 1
    
    return count