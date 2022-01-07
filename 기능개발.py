import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    time = deque()
    for i in range(len(progresses)):
        temp = math.ceil((100 - progresses[i])/speeds[i]) # (//) 로 계산하면 안됨!!
        time.append(temp)
    q = deque()
    if len(time)==1:
        answer.append(time[0])
    else:
        q.append(time.popleft())
        while time:
            stack_bottom = q[0]
            push = time.popleft()
            if stack_bottom >= push:
                q.append(push)
            else:
                answer.append(len(q))
                q.clear()
                q.append(push)
        if len(q)>0:
            answer.append(len(q))
    return answer
