def gcd(a, b):
    while b!=0:
        a, b = b, a%b
        
    return a

def solution(n, m):
    gcdNum = gcd(n, m)
    
    return [gcdNum, (n*m)/gcdNum]