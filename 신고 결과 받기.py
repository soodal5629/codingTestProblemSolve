from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    d = defaultdict(list)
    for i in report:
        a,b = i.split()
        if a not in d[b]:
            d[b].append(a)
    d2 = defaultdict(list)
    for i in report:
        a,b = i.split()
        if b not in d2[a]: d2[a].append(b)
    temp = []
    for i in id_list:
        if len(d[i])>=k:
            temp.append(i)
    for i in id_list:
        cnt = 0
        for j in temp:
            if j in d2[i]: 
                cnt+=1
        answer.append(cnt)
    return answer
