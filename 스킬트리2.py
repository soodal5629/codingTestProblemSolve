def solution(skill, skill_trees):
    answer = 0
    arr = [i for i in skill]
    arr2 = []
    for i in skill_trees:
        temp = ''
        for j in i:
            if j in arr:
                temp += j
        arr2.append(temp)
    for i in arr2:
        if i == '':
            answer +=1
            continue
        if i in skill:
            if skill[0] not in i: continue
            answer+=1
    return answer
