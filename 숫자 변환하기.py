from collections import deque
def solution(x, y, n):
    answer = -1
    if x == y: return 0
    cnt = 1
    d = deque()
    d.append(x)
    visit = [0] * 1000001
    while d:
        x = d.popleft()
        if x * 2 <= y and x*2 < 1000001 and visit[x*2] == 0:
            if x*2 == y:
                answer = visit[x] +1
                break
            visit[x*2] = visit[x] + 1
            d.append(x*2)
        if x*3 <= y:
            if x*3 == y and x*3 < 1000001 and visit[x*3] == 0:
                answer = visit[x]+1
                break
            visit[x*3] = visit[x] +1
            d.append(x*3)
        if x + n <= y and (x+n) < 1000001 and visit[x+n] == 0:
            if x+n == y:
                answer = visit[x]+1
                break
            visit[x+n] = visit[x] +1
            d.append(x+n)
    return answer
