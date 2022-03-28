from collections import deque
def solution(N, road, K):
    answer = 1
    graph = [[] for _ in range(N+1)]
    distance = [1e9] * (N+1)
    distance[1] =  0
    for i in road:
        a, b, c = i
        graph[a].append((c, b))
        graph[b].append((c, a))
    start = 1
    d = deque()
    d.append(start)
    visit = [False] * (N+1)
    while d:
        start = d.popleft()
        visit[start] = True
        for i in graph[start]:
            cost, b = i
            if distance[b] > cost+distance[start]:
                distance[b] = cost+distance[start]
                d.append(b)
    for i in range(2, N+1):
        if distance[i]<=K: answer+=1
    return answer
