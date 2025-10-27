def solution(arr1, arr2):
    arr3 = []
    
    for a1, a2 in zip(arr1, arr2):
        arr3.append([a+b for a, b in zip(a1, a2)])
    
    return arr3