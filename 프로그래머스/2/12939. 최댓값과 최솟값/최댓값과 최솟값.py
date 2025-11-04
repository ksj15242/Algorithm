def solution(s):
    sList = list(map(int, s.split()))
    
    return f'{min(sList)} {max(sList)}'