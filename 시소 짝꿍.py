from collections import Counter
def solution(weights):
    answer = 0
    c = Counter(weights)
    for i in c.keys():
        answer += ((c[i] * (c[i]-1)) // 2)
    s = set()
    for i in c.keys():
        for j in [1/2, 2/3, 3/4]:
            temp = i * j
            if temp in weights:
                answer += (c[i] * c[i*j])
    return answer
