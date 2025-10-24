def solution(n, w, num):
    popCount = 0
    boxNum = num
    
    while boxNum<=n:
        popCount += 1
        row = (boxNum-1)//w
        boxNum += ((row+1)*w-boxNum)*2+1
    
    return popCount