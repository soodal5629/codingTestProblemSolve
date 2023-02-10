from collections import defaultdict
def get_time(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)

def solution(fees, records):
    answer = []
    
    arr = []
    d = defaultdict(list)
    base, fee, unit, add = fees
    for i in records:
        arr.append(i.split(" "))
    arr.sort()
    cost = defaultdict(int)
    for i in arr:
        d[i[1]].append([i[0], i[2]])
        cost[i[1]] = 0
    for k, v in d.items():
        temp = 0
        for i, value in enumerate(v):
            time, type = value
            if type == 'OUT':
                temp += get_time(time) 
            elif i != len(v)-1 and type == 'IN':
                temp -= get_time(time)
            elif i == len(v)-1 and type == 'IN':
                temp += (get_time('23:59') - get_time(time))
        if temp > base:
            if (temp - base)%unit == 0:
                cost[k] = (fee + ((temp - base)//unit) * add)
            else:
                cost[k] = (fee + ((temp - base)//unit +1) * add)
        else: cost[k] = fee
    test = sorted(cost.keys())
    for i in test:
        answer.append(cost[i])
    return answer
