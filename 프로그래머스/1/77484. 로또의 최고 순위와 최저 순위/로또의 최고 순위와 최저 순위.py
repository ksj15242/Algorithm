def solution(lottos, win_nums):
    lottoRank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    winLottos = set(win_nums)
    zeroCount = lottos.count(0)
    matchedCount = sum(1 for num in lottos if num in winLottos)
    
    minMatched = matchedCount
    maxMatched = matchedCount + zeroCount
    
    return [lottoRank[maxMatched], lottoRank[minMatched]]