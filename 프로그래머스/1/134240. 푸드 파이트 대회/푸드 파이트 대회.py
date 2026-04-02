def solution(food):
    n = len(food)
    
    firstArrange = ""
    for i in range(1, n):
        firstArrange += str(i)*(food[i]//2)
    
    secondArrange = firstArrange[::-1]
    foodArrange = firstArrange + "0" + secondArrange
    
    return foodArrange
    