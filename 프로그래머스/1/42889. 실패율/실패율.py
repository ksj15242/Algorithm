def solution(N, stages):
    n = len(stages)
    stageInPlayers = {i:0 for i in range(N+2)}
    
    for stage in stages:
        stageInPlayers[stage] += 1
    
    tryPlayers = n
    failureRate = []
    for i in range(1, N+1):
        tryPlayers -= stageInPlayers[i-1]
        
        if tryPlayers==0:
            failure = 0
        else:
            failure = stageInPlayers[i]/tryPlayers
            
        failureRate.append((i, failure))
    
    failureRate.sort(key=lambda x:-x[1])
    answer = [stage for stage, rate in failureRate]
    
    return answer