from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    d = defaultdict(int)
    for i in range(len(name)):
        d[name[i]] = yearning[i]
    for i in photo:
        temp = 0
        for j in i:
            temp += d[j]
        answer.append(temp)
    return answer
