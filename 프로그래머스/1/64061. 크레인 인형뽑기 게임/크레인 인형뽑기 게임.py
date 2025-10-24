def getFigure(board, idx):
    n = len(board)
    
    figure = 0
    for i in range(n):
        if board[i][idx]!=0:
            figure = board[i][idx]
            board[i][idx] = 0
            break
    
    return figure

def getRemovedFigureCount(stack):
    removedCount = 0
    
    while len(stack)>=2:
        if stack[-2]!=stack[-1]:
            break
        
        stack.pop()
        stack.pop()
        removedCount += 2
            
    return removedCount

def solution(board, moves):
    figureStack = []
    removedFigures = 0
    
    for move in moves:
        figure = getFigure(board, move-1)
        
        if figure!=0:
            figureStack.append(figure)
            removedFigures += getRemovedFigureCount(figureStack)
        
    return removedFigures