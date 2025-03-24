def solution(name, yearning, photo):
    answer = []
    
    name_yearning = dict(zip(name, yearning))
    
    for shot in photo:
        score = 0
        for person in shot:
            try:
                score += name_yearning[person]
            except:
                continue
        answer.append(score)
    
    
    return answer