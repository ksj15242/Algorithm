def solution(X, Y):
    xNumCount = {str(i):0 for i in range(0, 10)}
    yNumCount = {str(i):0 for i in range(0, 10)}
    
    for x in X:
        xNumCount[x] += 1
        
    for y in Y:
        yNumCount[y] += 1
    
    mate = ""
    for i in range(9, -1, -1):
        repeat = min(xNumCount[str(i)], yNumCount[str(i)])
        mate += str(i)*repeat

    if mate=="":
        return "-1"
    
    if mate[0]=='0':
        return "0"

    return mate