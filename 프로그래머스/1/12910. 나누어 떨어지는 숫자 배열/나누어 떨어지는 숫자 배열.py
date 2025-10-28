def solution(arr, divisor):    
    arr.sort()
    
    answer = []
    for n in arr:
        if n%divisor == 0:
            answer.append(n)
    
    return answer if answer else [-1]