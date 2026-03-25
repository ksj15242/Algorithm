def integral_points(k):
    prefix = [0]
    prev = k
    
    while k>1:
        if k%2==0:
            k //= 2
        else:
            k = k*3+1
        
        prefix.append(prefix[-1]+(prev+k)/2)
        prev = k
    
    return prefix

def solution(k, ranges):
    integrals = integral_points(k)
    n = len(integrals)-1
    
    answer = []
    for s, b in ranges:
        e = n+b

        if s>e:
            answer.append(-1)
        else:
            answer.append(integrals[e]-integrals[s])
    
    return answer