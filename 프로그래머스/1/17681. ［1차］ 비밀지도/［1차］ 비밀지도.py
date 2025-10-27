def solution(n, arr1, arr2):
    answer = []
    
    for s1, s2 in zip(arr1, arr2):
        binary = format(s1|s2, f'0{n}b')
        decode = ''.join('#' if c=='1' else ' ' for c in binary )
        
        answer.append(decode)
    
    return answer