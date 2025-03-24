def solution(data, ext, val_ext, sort_by):
    answer = []
    sort_param = dict(enumerate(['code', 'date', 'maximum', 'remain']))
    sort_param = {v:k for k, v in sort_param.items()}
    
    for dat in data:
        if dat[sort_param[ext]] < val_ext:
            answer.append(dat)
    
    answer.sort(key = lambda x : x[sort_param[sort_by]])
    
    return answer