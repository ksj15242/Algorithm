from itertools import combinations

def isPrimeNumber(n):
    sqrt = int(n**0.5)+1
    
    for i in range(2, sqrt):
        if n%i==0:
            return False
    
    return True

def solution(nums):
    primes = set()
    selectList = combinations(nums, 3)
    count = 0
    
    for select in selectList:
        sumNum = sum(select)
            
        if sumNum in primes:
            count += 1
            continue
            
        if isPrimeNumber(sumNum):
            primes.add(sumNum)
            count += 1
                
    return count