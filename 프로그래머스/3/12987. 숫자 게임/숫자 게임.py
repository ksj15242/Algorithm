def solution(A, B):
    n = len(A)
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    score = 0
    idx = 0
    
    for i in range(n):
        if A[i]<B[idx]:
            idx += 1
            score += 1

    return score