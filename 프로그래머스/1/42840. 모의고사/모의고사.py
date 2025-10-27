def solution(answers):
    method1 = (1, 2, 3, 4, 5)
    method2 = (2, 1, 2, 3, 2, 4, 2, 5)
    method3 = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    
    n1, n2, n3 = len(method1), len(method2), len(method3)
    matchedCount = [0]*3
    
    for i, answer in enumerate(answers):
        if method1[i%n1]==answer:
            matchedCount[0] += 1
        
        if method2[i%n2]==answer:
            matchedCount[1] += 1
        
        if method3[i%n3]==answer:
            matchedCount[2] += 1
    
    maxCount = max(matchedCount)
    
    answer = []
    for i, count in enumerate(matchedCount):
        if maxCount==count:
            answer.append(i+1)
    
    return answer