def solution(s):
    n = len(s)
    mid = n//2
    
    if n%2==0:
        return s[mid-1]+s[mid]
    
    return s[mid]