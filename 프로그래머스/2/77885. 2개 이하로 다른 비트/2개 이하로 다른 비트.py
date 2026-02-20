def solution(numbers):
    answer = []
    
    for number in numbers:
        if number%2==0:
            answer.append(number+1)
        else:
            n = number
            k = 0
            while n&1:
                k += 1
                n >>= 1
                
            answer.append((number+1) | ((1<<(k-1))-1))
            
    return answer