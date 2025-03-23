def solution(bandage, health, attacks):
    curr = health
    curr_time = 0
    accum = 0
    attack_t = 0
    
    for time in range(attacks[-1][0]):
        # attacked
        if time == attacks[attack_t][0] - 1:
            curr -= attacks[attack_t][1]
            attack_t += 1
            accum = 0
            if curr <= 0:
                curr = -1
                break
            continue
        else:
            # cure
            curr = min(health, curr + bandage[1])
            accum += 1
            if accum == bandage[0]:
                curr = min(health, curr + bandage[2])
                accum = 0
        
    
    return curr