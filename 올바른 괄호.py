from collections import deque
def solution(s):
    answer = True
    d = deque()
    d.append(s[0])
    for i in range(1, len(s)):
        if d: top = d[-1]
        else: 
            d.append(s[i])
            continue
        if top == "(" and s[i] == ")": d.pop()
        else:
            d.append(s[i])
    if d: answer = False
    else: answer = True
    return answer
