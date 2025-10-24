def solution(players, callings):
    rank = {}
    for i, player in enumerate(players):
        rank[player] = i
    
    for callPlayer in callings:
        callRank = rank[callPlayer]
        aheadPlayer = players[callRank-1]
        
        players[callRank-1], players[callRank] = players[callRank], players[callRank-1]
        rank[callPlayer], rank[aheadPlayer] = rank[aheadPlayer], rank[callPlayer]
         
    return players