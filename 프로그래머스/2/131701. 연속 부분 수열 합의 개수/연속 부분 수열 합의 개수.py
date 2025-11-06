def solution(elements):
    n = len(elements)
    
    arr = elements*2
    prefixSum = [0]
    for num in arr:
        prefixSum.append(prefixSum[-1]+num)
        
    sumSet = set()
    for i in range(1, n+1):
        for j in range(n):
            sumSet.add(prefixSum[j+i]-prefixSum[j])
    
    return len(sumSet)