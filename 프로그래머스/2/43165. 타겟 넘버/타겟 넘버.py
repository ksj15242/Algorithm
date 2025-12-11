def dfs(i, cur, target, nums):
    if i==len(nums)-1:
        return 1 if cur==target else 0
    
    return dfs(i+1, cur+nums[i+1], target, nums) + dfs(i+1, cur-nums[i+1], target, nums)

def solution(numbers, target):
    return dfs(0, numbers[0], target, numbers) + dfs(0, -numbers[0], target, numbers)