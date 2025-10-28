def solution(nums):
    types = len(set(nums))
    getBowl = len(nums)//2
    
    return getBowl if types>=getBowl else types