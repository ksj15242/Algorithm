def is_prime(n):
    if n<2:
        return False
    if n%2==0:
        return n==2
    
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
        
    return True

def dfs(nums, visited, cur_num, primes, checked):
    if cur_num:
        num = int(cur_num)
        
        if num not in checked:
            checked.add(num)
            
            if is_prime(num):
                primes.add(num)
    
    for i in range(len(nums)):
        if visited[i]:
            continue
        
        visited[i] = True
        dfs(nums, visited, cur_num+nums[i], primes, checked)
        visited[i] = False
        
def solution(numbers):
    nums = list(numbers)
    visited = [False]*len(nums)
    primes = set()
    checked = set()
    
    dfs(nums, visited, "", primes, checked)
    
    return len(primes)