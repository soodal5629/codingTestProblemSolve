from collections import defaultdict
def topology(s, d,g):
    temp = {}
    for i in d:
        temp[i] = d[i]
    temp_g = defaultdict(list)
    for i in g:
        temp_g[i] = g[i]
    for i, value in enumerate(s):
        if temp[value] == 0:
            for j in temp_g[value]:
                temp[j] -= 1
        else: return False
    return True
def solution(skill, skill_trees):
    answer = 0
    d = {}
    g = defaultdict(list)
    for i, value in enumerate(skill):
        if i == 0: d[value] = 0
        else: d[value] = 1
        if i<len(skill)-1:
            g[value].append(skill[i+1])
    arr = []
    for i in skill_trees:
        for index,  value in enumerate(i):
            if value not in d.keys():
                i = i.replace(value, "")
        arr.append(i)
    for i in arr:
        if topology(i, d, g): answer+=1
    return answer
