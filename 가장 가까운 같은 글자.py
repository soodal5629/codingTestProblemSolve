from collections import defaultdict
def solution(s):
    answer = []
    d = defaultdict(int)
    temp = set(s)
    for i in temp:
        d[i] = s.index(i)
    for i,v in enumerate(s):
        if i == d[v]:
            answer.append(-1)
        else:
            answer.append(i - d[v])
            d[v] = i
    return answer
