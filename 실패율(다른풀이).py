from collections import Counter, defaultdict
def solution(N, stages):
    answer = []
    l = len(stages)
    c = Counter(stages)
    d = defaultdict(float)
    for i in range(1, N+1):
        if l > 0: 
            d[i] = c[i]/l
            l -= c[i]
        else: d[i] = 0
    d1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
    for i in d1:
        answer.append(i[0])
    return answer
