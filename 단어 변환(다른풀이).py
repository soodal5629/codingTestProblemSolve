from collections import deque
def check(s, now):
    cnt =  0
    for i in range(len(now)):
        if now[i] != s[i]: cnt+=1
    return cnt
def solution(begin, target, words):
    answer = 0
    if target not in words: return 0
    d = deque()
    temp = []
    temp.append(begin)
    d.append((begin, 0))
    while d:
        now, cost = d.popleft()
        if now == target:
            return answer
        for i in words:
            if i in temp: continue
            cnt = check(i, now)
            if cnt == 1:
                d.append((i, cost+1))
                answer = cost+1
                temp.append(i)
    return answer
