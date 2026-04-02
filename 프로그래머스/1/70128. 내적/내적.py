def solution(a, b):
    dotProduct = 0
    
    for n1, n2 in zip(a, b):
        dotProduct += n1*n2
    
    return dotProduct