from collections import deque

answer = 0

def dfs(state, dungeons, visited, count):
    global answer
    answer = max(answer, count)
    
    for i, (need, use) in enumerate(dungeons):
        if not visited[i] and state>=need:
            visited[i] = True
            dfs(state-use, dungeons, visited, count+1)
            visited[i] = False

def solution(k, dungeons):
    n = len(dungeons)
    visited = [False]*n
    
    dfs(k, dungeons, visited, 0)
    
    return answer