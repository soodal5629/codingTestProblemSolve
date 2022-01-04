from collections import defaultdict
def solution(clothes):
    answer = 0
    combi = defaultdict(list)
    for key, value in clothes:
        combi[value].append(key)
        answer+=1
    key_len = len(combi.keys())
    answer = 1
    for key in combi.keys():
        answer *= (len(combi[key])+1)
    answer -=1
    return answer
