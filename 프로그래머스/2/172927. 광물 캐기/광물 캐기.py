def solution(picks, minerals):
    minerals = minerals[:sum(picks) * 5]
    n = len(minerals)
    
    costs = []
    for i in range(0, n, 5):
        chunk = minerals[i:i+5]
        di = chunk.count("diamond")
        ir = chunk.count("iron")
        st = chunk.count("stone")
        
        costs.append((di, ir, st))        
    
    costs.sort(key=lambda x : (-x[0], -x[1], -x[2]))

    answer = 0
    for di, ir, st in costs:
        if picks[0]>0:
            answer += di+ir+st
            picks[0] -= 1
        elif picks[1]>0:
            answer += di*5+ir+st
            picks[1] -= 1
        else:
            answer += di*25+ir*5+st
            picks[2] -= 1

    return answer