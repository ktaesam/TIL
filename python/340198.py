def solution(mats, park):
    answer = -1
    
    # 내림차순 정렬
    mats.sort(reverse = True)
    

    
    for length in mats:
        for i in range(len(park) - length + 1):
            for j in range(len(park[i]) - length + 1):
                
                # 확인 절차
                success = 0
                for x in range(length):
                    if len(''.join(park[i + x][j:j + length])) == length * 2:
                        success += 1
                if success == length:
                    answer = length
                    break
                    
            if answer > 0:
                break
        if answer > 0:
            break
    
    return answer