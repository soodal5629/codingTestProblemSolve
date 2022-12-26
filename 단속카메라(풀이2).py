def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    for i, v in enumerate(routes):
        if i == 0: 
            answer+=1
            point = v[1]
            continue
        if v[0] <= point <= v[1]:
            continue
        else:
            point = v[1]
            answer+=1
    return answer
