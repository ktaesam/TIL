# string을 second로 변환
def str2second(target):
    return int(target[:2]) * 60 + int(target[3:])

# second를 string으로 변환
def second2str(target):
    minute = str(target // 60)
    second = str(target % 60)
    minute = (2 - len(minute)) * '0' + minute
    second = (2 - len(second)) * '0' + second
    return minute + ':' + second

def solution(video_len, pos, op_start, op_end, commands):
    video_len_t = str2second(video_len)
    pos_t = str2second(pos)
    op_start_t = str2second(op_start)
    op_end_t = str2second(op_end)
    
    # 오프닝 스킵
    if (pos_t >= op_start_t) and (pos_t <= op_end_t):
        pos_t = op_end_t
    
    for command in commands:
        if command == 'prev':
            pos_t = max(0, pos_t - 10)
        elif command == 'next':
            pos_t = min(video_len_t, pos_t + 10)
        # 오프닝 스킵
        if (pos_t >= op_start_t) and (pos_t <= op_end_t):
            pos_t = op_end_t
            
    answer = second2str(pos_t)
    return answer