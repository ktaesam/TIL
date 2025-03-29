def solution(n, m, section):
    answer = 0
    
    wall = [1] * n
    
    for idx in section:
        wall[idx - 1] = 0
    
    '''
    while sum(wall) != n:
        start = wall.index(0)
        for i in range(m):
            if start + i < n:
                wall[start + i] = 1
        answer += 1
    '''
    
    paint = [0, m]
    
    for i in range(n):
        # print(wall)
        if paint[0] == 1:
            wall[i] = 1
            paint[1] -= 1    
        elif wall[i] == 0:
            paint[0] = 1
            wall[i] = 1
            paint[1] -= 1
            answer += 1
        
        if paint[1] == 0:
            paint[0] = 0
            paint[1] = m
    
    
    return answer