def solution(n):
    primes = [True]*(n+1)
    primes[0], primes[1] = False, False

    sqrt = int(n**0.5)
    
    for i in range(2, sqrt+1):
        if not primes[i]:
            continue
        
        for j in range(i*i, n+1, i):
            primes[j] = False
    
    return primes.count(True)