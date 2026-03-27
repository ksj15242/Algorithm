def solution(s):
    n = len(s)
    answer = n

    for i in range(1, n//2+1):
        cnt = 0
        compressed_len  = 0
        prev = s[:i]

        for j in range(i, n+1, i):
            cur = s[j:j+i]

            if prev != cur:
                compressed_len  += len(prev) if cnt==0 else len(str(cnt+1)) + len(prev)
                prev = cur
                cnt = 0
            else:
                cnt += 1

        compressed_len  += len(prev) if cnt == 0 else len(str(cnt+1)) + len(prev)
        
        answer = min(answer, compressed_len )

    return answer