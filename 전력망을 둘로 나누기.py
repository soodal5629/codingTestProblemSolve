def dfs(x, y, graph):
    s = [x]
    cnt = 1
    cnt2= 0
    visit = [False] * (len(graph)+1)
    while s:
        now = s.pop()
        visit[now] = True
        for i in graph[now]:
            if i == x: continue
            elif i == y: continue
            else:
                if visit[i]: continue
                s.append(i)
                cnt += 1
    return cnt
def solution(n, wires):
    answer = 1e9
    g = [[] for _ in range(n+1)] 
    for i in wires:
        a, b = i
        g[a].append(b)
        g[b].append(a)
    for i in range(1, n+1):
        for j in g[i]:
            cnt = dfs(i, j, g)
            remainder = abs(n-cnt)
            if answer >= abs(remainder - cnt):
                answer = abs(remainder-cnt)
    return answer
