from collections import deque
def solution(s):
    answer = 0
    d = deque()
    for i, v in enumerate(s):
        if len(d)==0: 
            d.append(v)
            continue
        else:
            if d[-1] == v:
                d.pop()
            else:
                d.append(v)
    if len(d)==0: answer = 1

    return answer
