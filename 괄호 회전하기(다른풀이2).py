from collections import deque
def find(s):
    temp = deque()
    temp.append(s.popleft())
    for i in s:
        if temp:
            top = temp[-1]
            if top == '(' and i == ')':
                temp.pop()
            elif top == '[' and i == ']':
                temp.pop()
            elif top == '{' and i == '}':
                temp.pop()
            else: temp.append(i)
        else:
            temp.append(i)
    if temp: return 0
    else: return 1

def solution(s):
    answer = 0
    n = len(s)
    s = deque(s)
    for i in range(n):
        temp = deque(s)
        answer += find(temp)
        s.append(s.popleft())
    return answer
