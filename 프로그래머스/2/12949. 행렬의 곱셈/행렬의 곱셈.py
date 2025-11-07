def solution(arr1, arr2):
    n, m, p = len(arr1), len(arr2[0]), len(arr1[0])
    answer = []
    
    for i in range(n):
        temp = []
        
        for j in range(m):
            sumNum = 0
            
            for k in range(p):
                sumNum += arr1[i][k]*arr2[k][j]
            
            temp.append(sumNum)
        
        answer.append(temp)
    
    return answer