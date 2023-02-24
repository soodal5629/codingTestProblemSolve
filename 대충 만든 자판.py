from collections import defaultdict
def solution(keymap, targets):
    answer = []
    d = defaultdict(int)
    for i in keymap:
        for j, v in enumerate(i):
            if d[v] == 0: # 처음 등장
                d[v] = j+1
            else:
                d[v] = min(d[v], j+1)
    for i in targets:
        temp = 0
        for j in i:
            temp += d[j]
        if temp == 0: temp = -1
        answer.append(temp)
    return answer
