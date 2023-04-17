def solution(targets):
    answer = 1
    targets.sort(key = lambda x:(x[0],x[1]))
    s, e = targets[0]
    for i in range(1, len(targets)):
        x, y = targets[i]
        if x < e:
            s = x
            if y <= e:
                e = y
        else:
            answer+=1
            s = x
            e = y
    return answer
