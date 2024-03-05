from collections import deque

def find(g, n, m, d):
  arr = []
  mini = 1e9
  q = deque()
  q.append((1, 0))
  v = [False] * (n+1)
  v[1] = True
  while q:
    now, cnt = q.popleft()
    for i in g[now]:
      if not v[i]:
        q.append((i, cnt+1))
        v[i] = True
        d[i] = cnt+1
  dist = -1
  for i in range(1, n+1):
    dist = max(dist, d[i])
  
  print(d.index(dist), dist, d.count(dist))
  
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)
d = [1e9] * (n+1)
d[0] = d[1] = 0
find(g, n, m, d)
