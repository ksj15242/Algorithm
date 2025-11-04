def solution(s):
    openCount = 0

    for c in s:
        if c=='(':
            openCount += 1
        elif c==')':
            openCount -= 1

        if openCount<0:
            break

    return openCount==0