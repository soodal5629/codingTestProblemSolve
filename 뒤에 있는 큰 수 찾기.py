from collections import deque
def solution(numbers):
    answer = [-1] * (len(numbers))
    d = deque()
    for i, v in enumerate(numbers):
        d.append([i,v])
    s = deque()
    s.append(d.popleft())
    for i in d:
        index, v = i
        if d:
            top = s[-1][1]      
            while v>top:
                answer[s[-1][0]] = v
                s.pop()
                if len(s)>0: top = s[-1][1]
                else: break
            s.append((index, v))
        else:
            s.append((index, v))
    return answer
