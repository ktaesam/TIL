def solution(players, callings):
    answer = []
    
    # 등수, 이름
    player_dict = dict(enumerate(players))
    # 이름, 등수
    player_dict_rev = {v : k for k, v in player_dict.items()}
    
    for call in callings:
        # 불린 사람의 등수
        call_rank = player_dict_rev[call]
        # 앞 사람 이름
        front_name = player_dict[call_rank - 1]
        
        # 최신화
        player_dict[call_rank - 1] = call
        player_dict[call_rank] = front_name
        player_dict_rev[call] -= 1
        player_dict_rev[front_name] += 1


    answer = sorted(player_dict_rev, key = lambda x : player_dict_rev[x])
        
    return answer