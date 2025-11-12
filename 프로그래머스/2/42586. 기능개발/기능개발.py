def solution(progresses, speeds):
    availableDays = []
    for progress, speed in zip(progresses, speeds):
        day = ((100-progress)+(speed-1))//speed
        availableDays.append(day)
    
    answer = []
    past = availableDays[0]
    count = 0
    for day in availableDays:
        if past>=day:
            count += 1
        else:
            answer.append(count)
            past = day
            count = 1
    
    answer.append(count)
    
    return answer