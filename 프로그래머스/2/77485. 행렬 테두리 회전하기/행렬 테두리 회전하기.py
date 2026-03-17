from collections import deque

def extract_and_rotate_nums(table, query):
    x1, y1, x2, y2 = [q-1 for q in query]
    
    que = deque([])
    
    for y in range(y1, y2+1):
        que.append(table[x1][y])
        
    for x in range(x1+1, x2+1):
        que.append(table[x][y2])
    
    for y in range(y2-1, y1-1, -1):
        que.append(table[x2][y])
    
    for x in range(x2-1, x1, -1):
        que.append(table[x][y1])
    
    que.appendleft(que.pop())
    
    return que

def apply_rotate_nums(table, query, que):
    x1, y1, x2, y2 = [q-1 for q in query]
    
    for y in range(y1, y2+1):
        table[x1][y] = que.popleft()
        
    for x in range(x1+1, x2+1):
        table[x][y2] = que.popleft()
    
    for y in range(y2-1, y1-1, -1):
        table[x2][y] = que.popleft()
    
    for x in range(x2-1, x1, -1):
        table[x][y1] = que.popleft()

def solution(rows, columns, queries):
    answer = []
    
    table = [[i*columns + j for j in range(1,columns+1)] for i in range(rows)]
    for query in queries:
        rotate_nums = extract_and_rotate_nums(table, query)
        answer.append(min(rotate_nums))
        apply_rotate_nums(table, query, rotate_nums)
    
    return answer