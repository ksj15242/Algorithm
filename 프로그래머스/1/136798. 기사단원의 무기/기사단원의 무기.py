def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number+1):
        count = 0
        sqrt = int(num**0.5)
        
        for i in range(1, sqrt+1):
            if num%i==0:
                count += 2
                
            if num/i==i:
                count -= 1
            
            if count>limit:
                count = power
                break

        answer += count
        
    return answer