def lcm(a, b):
    na, nb = a, b
    
    while nb:
        na, nb = nb, na%nb
        
    return a*b//na

def solution(arr):
    lcmNum = arr[0]
    
    for num in arr[1:]:
        lcmNum = lcm(lcmNum, num)
    
    return lcmNum