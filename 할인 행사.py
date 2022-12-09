from collections import defaultdict
def solution(want, number, discount):
    answer = 0
    d1 = defaultdict(int)
    for i in range(len(want)):
        d1[want[i]] = number[i]
    d2 = defaultdict(int)
    index = 0
    next = index+9
    for i in discount[0:10]:
        d2[i] += 1
    while(next < len(discount)):
        flag = True
        for i in want:
            if d1[i] != d2[i]:
                flag = False
                break
        if flag :
            answer+=1
        d2[discount[index]]-=1
        index+=1
        next = index+9
        if next <len(discount): d2[discount[next]]+=1
    return answer
