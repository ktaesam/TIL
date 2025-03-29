def solution(keymap, targets):
    answer = []
    
    alphabets = [101] * 26
    
    for keys in keymap:
        for i in range(len(keys)):
            key = keys[i]
            alphabets[ord(key) - 65] = min(alphabets[ord(key) - 65], i + 1)
            
    # print(alphabets)
    
    for target in targets:
        cnt = 0
        
        for each in target:
            cnt += alphabets[ord(each) - 65]
            if alphabets[ord(each) - 65] == 101:
                cnt = -1
                break
                
        answer.append(cnt)
    return answer