from collections import deque

def bfs(g, n):
  v = [False] * (n+1)
  d = deque()
  d.append(1)
  p = [0] * (n+1)
  p[1] = 1
  while d:
    now = d.popleft()
    v[now] = True
    for i in g[now]:
      if not v[i]:
        d.append(i)
        v[i] = True
        p[i] = now
  for i in range(2, len(p)):
    print(p[i])
  
n = int(input())
g = [[] for _ in range(n+1)]
for i in range(n-1):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

bfs(g, n)
