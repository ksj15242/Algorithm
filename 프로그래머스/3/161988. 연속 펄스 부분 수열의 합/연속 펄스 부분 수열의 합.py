def solution(sequence):
    answer = 0
    
    prefix1 = 0
    prefix2 = 0
    min_prefix1 = 0
    min_prefix2 = 0

    for i, x in enumerate(sequence):
        if i % 2 == 0:
            prefix1 += x
            prefix2 -= x
        else:
            prefix1 -= x
            prefix2 += x

        answer = max(answer, prefix1-min_prefix1, prefix2-min_prefix2)
        
        min_prefix1 = min(min_prefix1, prefix1)
        min_prefix2 = min(min_prefix2, prefix2)

    return answer