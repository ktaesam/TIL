def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(timelogs)):
        # 시작 날짜
        today = startday - 1
        # 성공 횟수
        score = 0
        # 목표 시간 분으로 환산
        due = (schedules[i] // 100) * 60 + (schedules[i] % 100)
        
        for j in range(7):
            # 주말 제외
            if (today == 5) or (today == 6):
                today = (today + 1) % 7
                continue
            
            # 도착 시간 분으로 환산
            attendance = (timelogs[i][j] // 100) * 60 + (timelogs[i][j] % 100)
            today = (today + 1) % 7
            # 출근 확인
            if attendance <= due + 10:
                score += 1
            else:
                break
            
        # 지각 안한 사람
        if score == 5:
            answer += 1
                
            
    return answer