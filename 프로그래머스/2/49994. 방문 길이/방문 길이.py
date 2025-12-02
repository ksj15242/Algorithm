def solution(dirs):
    n = 10
    curX, curY = 5, 5
    
    mv = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
    savePaths = set()
    
    for dirKey in dirs:
        mx, my = mv[dirKey]
        nextX, nextY = curX+mx, curY+my
        
        if 0<=nextX<=n and 0<=nextY<=n:
            savePaths.add((curX, curY, nextX, nextY))
            savePaths.add((nextX, nextY, curX, curY))
            
            curX, curY = nextX, nextY
            
    return len(savePaths)//2