def solution(schedules, timelogs, startday):
    answer = 0
    
    for schedule, logs in zip(schedules, timelogs):
        hour = schedule//100
        minute = schedule%100
        minute += 10
        
        if minute >=60:
            minute -=60
            hour = (hour+1)%24
        
        startTime = hour*100 + minute
        late = False
        
        for i, arrival in enumerate(logs):
            day = (startday+i)%7
            
            if day in (0, 6):
                continue
            
            if arrival>startTime:
                late = True
                break
        
        if not late:
            answer += 1
    
    return answer