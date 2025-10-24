def solution(numbers):
    n = len(numbers)
    
    numberSet = set()
    for i in range(n):
        for j in range(i+1, n):
            numberSet.add(numbers[i]+numbers[j])
        
    numberList = list(numberSet)
    numberList.sort()
    
    return numberList