def getMultiCountSet(s):
    n = len(s)
    
    dic = {}
    for i in range(n-1):
        st = (s[i]+s[i+1]).lower()
        
        if st.isalpha() and st.isascii():
            dic[st] = dic.get(st,0)+1
    
    return dic

def solution(str1, str2):
    multiplier = 65536
    jaccard = [0,0]
    
    dic1 = getMultiCountSet(str1)
    dic2 = getMultiCountSet(str2)
    
    keySet = set(dic1.keys()) | set(dic2.keys())
    for key in keySet:
        s1, s2 = dic1.get(key,0), dic2.get(key,0)
        
        jaccard[0] += min(s1, s2)
        jaccard[1] += max(s1, s2)
        
    if jaccard[1]==0:
        return multiplier
    
    return int(jaccard[0]/jaccard[1]*multiplier)