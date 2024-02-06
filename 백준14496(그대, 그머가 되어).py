from collections import deque
def bfs(g, a, b, v):
  d = deque()
  d.append((a, 0))
  while d:
    now, cnt = d.popleft()
    v[now] = True
    if now == b:
      return cnt
    for i in g[now]:
      if not v[i]:
        d.append((i, cnt+1))
        v[i] = True
  return -1
a, b = map(int, input().split())
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
v = [False for _ in range(n+1)]
for i in range(m):
  x, y = map(int, input().split())
  g[x].append(y)
  g[y].append(x)
print(bfs(g, a, b, v))
