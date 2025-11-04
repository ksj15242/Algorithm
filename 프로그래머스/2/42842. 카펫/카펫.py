def solution(brown, yellow):
    totalGrids = brown+yellow
    sqrt = int(totalGrids**0.5)
    
    for height in range(3, sqrt+1):
        if totalGrids%height!=0:
            continue
        
        width = totalGrids//height
        
        if (height-2)*(width-2)==yellow:
            return [width, height]
    
    return [-1, -1]