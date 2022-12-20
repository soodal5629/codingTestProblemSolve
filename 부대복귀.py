from collections import deque
def bfs(g, dest, n, index, cost, sources):
    d = deque()
    d.append((0, dest))
    visit = [False] * (n+1)
    while d:
        c, now = d.popleft()
        if now in sources and visit[now] ==False:
            cost[now] = c
        visit[now] = True
        for i in g[now]:
            if visit[i]: continue
            d.append((c+1, i))
    return cost
def solution(n, roads, sources, destination):
    answer = []
    
    f=[[] for _ in range(n+1)]
    for i in roads:
        a, b = i
        f[a].append(b)
        f[b].append(a)
    cost = [-1] * (n+1)
    temp = bfs(f, destination, n, i, cost, sources)
    for i in sources:
        answer.append(temp[i])
    return answer
