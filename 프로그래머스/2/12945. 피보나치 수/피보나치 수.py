def solution(n):
    num = 1234567
    fibo = [0]*(n+1)
    fibo[1] = 1
    
    for i in range(2, n+1):
        fibo[i] = (fibo[i-1]+fibo[i-2])%num
    
    return fibo[n]