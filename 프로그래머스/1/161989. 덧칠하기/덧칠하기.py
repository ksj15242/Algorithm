def solution(n, m, section):
    paintCount = 0
    endPoint = 0

    for newPoint in section:
        if endPoint<newPoint:
            endPoint = newPoint+m-1
            paintCount += 1
    
    return paintCount