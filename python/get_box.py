def solution(n, w, num):
    answer = 0
    box_height = [0 for i in range(w)]
    direction = 0
    for i in range(1, n+1):
        # set direction
        if i % w == 1:
            direction += 1
        # find index
        if direction % 2 == 1:
            index = i % w - 1
        else:
            index = (w - (i % w)) % w
            
        if i == num:
            box_height[index] = 0
            answer = index
            
        box_height[index] += 1
        
    answer = box_height[answer]
    return answers