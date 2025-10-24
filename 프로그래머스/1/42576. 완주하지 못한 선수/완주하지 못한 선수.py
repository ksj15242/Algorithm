def solution(participant, completion):
    playersInfo = {}
    for name in participant:
        playersInfo[name] = playersInfo.get(name, 0)+1
        
    for name in completion:
        playersInfo[name] -= 1
    
    for name, count in playersInfo.items():
        if count==1:
            return name
    
    return ""