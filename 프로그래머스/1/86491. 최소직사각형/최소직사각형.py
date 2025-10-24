def solution(sizes):
    width = 0
    height = 0
    
    for w, h in sizes:
        width = max(width, max(w, h))
        height = max(height, min(w, h))
        
    return width*height