def solution(friends, gifts):
    answer = 0
    
    # 주고받음 확인용
    gift_list = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    # 선물 지수
    gift_idx = [0] * len(friends)
    # 매핑 테이블
    friends_idx = dict(enumerate(friends))
    friends_idx = {v : k for k, v in friends_idx.items()}

    # 선물 주고 받기    
    for gift in gifts:
        gift = gift.split()
        gift_from = gift[0]
        gift_to = gift[-1]
        gift_from = friends_idx[gift_from]
        gift_to = friends_idx[gift_to]
        
        # 주고 받기
        gift_list[gift_from][gift_to] += 1
        
        # 선물 지수
        gift_idx[gift_from] += 1
        gift_idx[gift_to] -= 1

        
    # 다음달 예상 받는 선물 개수
    next_gift = [0] * len(friends)
    
    # 다음달 선물 계산
    for a in range(len(friends)):
        for b in range(a, len(friends)):
            # a가 b한테 준 선물이 많을 때
            if gift_list[a][b] > gift_list[b][a]:
                next_gift[a] += 1
            # b가 a한테 준 선물이 많을 때
            elif gift_list[a][b] < gift_list[b][a]:
                next_gift[b] += 1
            # 같을 때
            else:
                if gift_idx[a] > gift_idx[b]:
                    next_gift[a] += 1
                elif gift_idx[a] < gift_idx[b]:
                    next_gift[b] += 1
    
    answer = max(next_gift)
    
    return answer