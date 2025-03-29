def solution(wallpaper):
    answer = []
    
    lux = len(wallpaper[0])
    luy = len(wallpaper)
    rdx = 0
    rdy = 0
    
        
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[0])):
            if wallpaper[y][x] == '#':
                lux = min(lux, x)
                luy = min(luy, y)
                rdx = max(rdx, x + 1)
                rdy = max(rdy, y + 1)
    
    answer = [luy, lux, rdy, rdx]
    
    return answer