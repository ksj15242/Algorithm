EMPTY = ''

def remove_blocks(m, n, board):
    removes = set()
    
    for x in range(m-1):
        for y in range(n-1):    
            if board[x][y]==EMPTY:
                continue
            
            if board[x][y]==board[x][y+1]==board[x+1][y]==board[x+1][y+1]:
                removes.update([(x,y),(x,y+1),(x+1,y),(x+1,y+1)])
    
    for x, y in removes:
        board[x][y] = EMPTY
    
    return len(removes)

def drop_blocks(m, n, board):
    for y in range(n):
        alives = []
        
        for x in range(m):
            if board[x][y]!='':
                alives.append(board[x][y])
        
        for x in range(m-1, -1, -1):
            if alives:
                board[x][y] = alives.pop()
            else:
                board[x][y] = EMPTY

def solution(m, n, board):
    answer = 0
    board = list(list(b) for b in board)

    while True:
        removed_count = remove_blocks(m, n, board)
        answer += removed_count
        
        if removed_count==0:
            break
            
        drop_blocks(m, n, board)
    
    return answer