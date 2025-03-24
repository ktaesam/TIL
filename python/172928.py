def solution(park, routes):
    answer = []
    
    ref = {'N' : [-1, 0],
           'E' : [0, 1],
           'W' : [0, -1],
           'S' : [1, 0]}
    curr = [0, 0]
    
    height = len(park)
    width = len(park[0])
    
    for i in range(height):
        if 'S' in park[i]:
            curr[0] = i
            curr[1] = park[i].index('S')
            break
    
    for route in routes:
        direction = route[0]
        count = int(route[-1])
        # 스킵 플래그
        skip = 0
        # 임시 좌표
        temp_y = curr[0]
        temp_x = curr[1]
        
        for _ in range(count):
            # 예상 좌표
            temp_y += ref[direction][0]
            temp_x += ref[direction][1]
            if temp_y < 0 or temp_x < 0:
                skip = 1
                break
            if temp_y  >= height or temp_x >= width:
                skip = 1
                break
            if park[temp_y][temp_x] == 'X':
                skip = 1
                break

        if skip:
            continue
            
        # 이동
        curr[0] = temp_y
        curr[1] = temp_x
                        
    answer = curr
    
    return answer