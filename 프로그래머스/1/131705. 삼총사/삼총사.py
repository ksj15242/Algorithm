def solution(number):
    n = len(number)
    
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if number[i]+number[j]+number[k]==0:
                    count += 1
                    
    return count