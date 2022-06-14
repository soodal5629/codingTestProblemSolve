from collections import deque
def solution(s):
    answer = 0
    d = []
    d.append(s[0])

    for i in range(1, len(s)):
        if d: 
            top = d[-1]
            if top == s[i]:
                d.pop()
            else:
                d.append(s[i])
        else: d.append(s[i])
    if d:
        answer = 0
    else: answer =1

    return answer
