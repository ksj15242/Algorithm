def solution(wallpaper):
    lux, luy = len(wallpaper), len(wallpaper[0])
    rdx, rdy = 0, 0

    for x, row in enumerate(wallpaper):
        for y, file in enumerate(row):
            if file == '#':
                lux, rdx = min(lux, x), max(rdx, x+1)
                luy, rdy = min(luy, y), max(rdy, y+1)
                
    return [lux, luy, rdx, rdy]