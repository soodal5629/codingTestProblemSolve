from collections import deque
def move(index, s):
    temp = ''
    first = s[0]
    if index == 0:
        return s
    else:
        temp  = s[1:]
        temp += first
        return temp
def check(s, d):
    stack = deque(s[0])
    if stack[-1] in [')', '}', ']']: 
        return 0
    for i in range(1, len(s)):
        if len(stack) == 0:
            if s[i] in [')', '}', ']']: 
                return 0
            stack.append(s[i])
            continue
        top = stack[-1]  
        if d[top] + d[s[i]] == 0 and top in ['(','[','{']:
            stack.pop()
        else:
            stack.append(s[i])
    if len(stack)>0: return 0
    else: return 1
def solution(s):
    answer = 0
    d={}
    d["("] = 1
    d[")"] = -1
    d["{"] = 2
    d["}"] = -2
    d["["] = 3
    d["]"] = -3
    for i in range(len(s)):
        s = move(i, s)
        answer += check(s, d)
    return answer
