def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliceArr = array[i-1:j]
        sliceArr.sort()
        answer.append(sliceArr[k-1])
    
    return answer
    