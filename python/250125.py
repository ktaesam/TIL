def solution(board, h, w):
    answer = 0
    # board 길이
    n = len(board)
    # 같은 색 count
    count = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if (0 <= h_check < n) and (0 <= w_check < n):
            if board[h][w] == board[h_check][w_check]:
                count += 1
                
    answer = count
    return answer