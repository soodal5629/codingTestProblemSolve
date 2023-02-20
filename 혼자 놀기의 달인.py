import copy
from collections import defaultdict
def pick(d, i, cards):
    res = 0
    d2 = d
    while True:
        if d2[i] == -1: break
        temp = i
        i = d2[i]
        d2[temp] = -1
        res+=1
    return res
def solution(cards):
    answer = 0
    d = defaultdict(int)
    for i in range(len(cards)):
        d[i+1] = cards[i]
    d2 = copy.deepcopy(d)
    for i in range(1, len(cards)+1):
        d = copy.deepcopy(d2)
        cnt1= pick(d, i, cards)
        cnt2= 0
        if cnt1 < len(cards):
            index = -1
            for j in d.keys():
                if d[j] != -1:
                    index = j
                    cnt2 = pick(d, index, cards)
                    answer = max(cnt1 * cnt2, answer)
    return answer
