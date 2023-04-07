from collections import defaultdict
def solution(players, callings):
    answer = []
    d = defaultdict(int)
    r = defaultdict(str)
    for i,v in enumerate(players):
        d[v] = i
        r[i] = v
    for i in callings:
        num = d[i]
        d[i] -=1
        d[r[num-1]] +=1 
        r[num] = r[num-1]
        r[num-1] = i
    for i in r.keys():
        answer.append(r[i])
    return answer
