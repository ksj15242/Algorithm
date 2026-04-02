def solution(ingredient):
    needStack = [1, 2, 3, 1]
    n = len(needStack)
    
    curStack = []
    burger = 0
    for curIngredient in ingredient:
        curStack.append(curIngredient)
        
        if len(curStack)>=n and curStack[-n:]==needStack:
            for _ in range(n):
                curStack.pop()
            burger += 1
            
    return burger