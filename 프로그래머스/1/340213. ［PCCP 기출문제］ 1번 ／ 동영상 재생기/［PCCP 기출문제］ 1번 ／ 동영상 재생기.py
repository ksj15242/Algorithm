# 단순 구현
# 시간 계산은 작은 단위로 변환해서 푸는게 가장 편하다

def timeToSecond(time):
    minute, second = time.split(":")
    
    return int(minute)*60+int(second)

def solution(video_len, pos, op_start, op_end, commands):
    videoEnd = timeToSecond(video_len)
    currentTime = timeToSecond(pos)
    openingStart = timeToSecond(op_start)
    openingEnd = timeToSecond(op_end)
    
    moveTime = {"next":10, "prev":-10}
    for command in commands:
        if openingStart<=currentTime<=openingEnd:
            currentTime = openingEnd
        
        currentTime += moveTime[command]
        if currentTime<0:
            currentTime = 0
        elif currentTime>videoEnd:
            currentTime = videoEnd
        
        if openingStart<=currentTime<=openingEnd:
            currentTime = openingEnd
    
    currentMinute = currentTime//60
    currentSecond = currentTime%60
    
    return f"{currentMinute:02}:{currentSecond:02}"