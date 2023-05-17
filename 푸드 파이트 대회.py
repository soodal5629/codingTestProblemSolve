from collections import defaultdict
def solution(food):
    answer = ''
    d = defaultdict(int)
    for i in range(len(food)):
        d[i] = food[i]
    for i in d.keys():
        if i == 0: continue
        answer += str(i)*(d[i]//2)
    temp = answer[::-1]
    answer+='0'
    answer+=temp
    return answer
