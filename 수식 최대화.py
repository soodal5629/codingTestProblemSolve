from itertools import permutations
from collections import deque

def find(priority, num):
    d = deque()
    num = deque(num)
    res = -1e9

    for i in priority:
        while num:
            if len(d)==0:
                d.append(num.popleft())
                continue
            d_top = d[-1]
            now = num.popleft()
            if now == i:
                d.pop()
                if now == '-':
                    d.append(d_top  - num.popleft())
                elif now == '+':
                    d.append(d_top  + num.popleft())
                else:  
                    d.append(d_top  * num.popleft())
            else:
                d.append(now)
        num = d
        d=deque()
    res = abs(num.pop())
    return res
  
def solution(expression):
    answer = 0
    e = list(permutations(['-','+','*'],3))
    num = []
    temp = ''
    for i,v in enumerate(expression):
        if i == len(expression)-1:
            temp+=v
            num.append(int(temp))
        if v not in ['-','+','*']:
            temp+=v
        else:
            num.append(int(temp))
            num.append(v)
            temp=''
    for i in e:
        res = find(i, num)
        answer = max(answer, res)
    return answer
