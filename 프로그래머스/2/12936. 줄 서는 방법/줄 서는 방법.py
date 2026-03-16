def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    
    return num
        
def solution(n, k):    
    answer = []
    
    nums = [i for i in range(1, n+1)]
    for i in range(1, n+1):
        facto = factorial(n-i)
        seq = (k+facto-1)//facto
        
        answer.append(nums.pop(seq-1))
        k -= (seq-1)*facto
                
    return answer