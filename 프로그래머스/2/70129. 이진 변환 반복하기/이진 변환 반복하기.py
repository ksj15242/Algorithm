def solution(s):
    convertCount = 0
    rmZeroCount = 0

    while s!='1':
                
        zeroCount = s.count('0')
        
        convertCount += 1
        rmZeroCount += zeroCount
        
        s = bin(len(s)-zeroCount)[2:]
        
    return [convertCount, rmZeroCount]