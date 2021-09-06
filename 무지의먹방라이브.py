from collections import deque
def solution(food, k):
    answer = 0
    index = 0
    q= deque()
    for i in food:
        q.append((index, i))
        index +=1
    while(k>0):
        index, now = q.popleft()
        if now>0:
            now -=1
            q.append((index,now))
            k-=1
        else: q.append((index,now))
    pos, answer =q.popleft() 
    while(answer<=0 and q):
        pos, answer =q.popleft()
    if answer<=0: answer = -1
    else: answer = pos+1
    return answer
