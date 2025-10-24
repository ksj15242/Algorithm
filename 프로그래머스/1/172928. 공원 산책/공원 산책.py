def findStartPosition(park, n, m):
    for i in range(n):
        for j in range(m):
            if park[i][j]=="S":
                return (i, j)
    
    return (-1,-1)

def solution(park, routes):
    n, m = len(park), len(park[0])
    direction = {'N':(-1,0), 'S':(1,0), 'W':(0,-1), 'E':(0,1)}
    curX, curY = findStartPosition(park, n, m)
    
    for route in routes:
        direct, space = route.split(" ")
        space = int(space)
        mvx, mvy = direction[direct]
        
        ignoreCommand = False
        for i in range(1, space+1):
            nextX, nextY = curX+mvx*i, curY+mvy*i
            
            if not (0<=nextX<n and 0<=nextY<m):
                ignoreCommand = True
                break
            
            if park[nextX][nextY]=='X':
                ignoreCommand = True
                break
        
        if not ignoreCommand:
            curX += mvx*space
            curY += mvy*space
        
    return [curX, curY]
            