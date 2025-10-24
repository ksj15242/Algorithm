def solution(board, h, w):
    count = 0
    n, m = len(board), len(board[0])
    
    findColor = board[h][w]
    checkList = [(h-1,w),(h+1,w),(h,w-1),(h,w+1)]
    for x, y in checkList:
        if 0<=x<n and 0<=y<m and board[x][y]==findColor:
            count += 1
            
    return count