def solution(clothes):
    clothesType = {}
    for _, ctype in clothes:
        clothesType[ctype] = clothesType.get(ctype, 0) + 1
    
    count = 1
    for num in clothesType.values():
        count *= num+1        
    
    count -= 1
    
    return count