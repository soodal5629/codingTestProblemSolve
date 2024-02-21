import sys
from collections import deque

def find(g, s, e, n, v, dist):
  d = deque()
  d.append((s, 0))
  v[s] = True
  dist[s] = 0
  while d:
    now, cnt = d.popleft()
    if now == e: return cnt
    for i in g[now]:
      if not v[i]:
        v[i] = True
        d.append((i, cnt+1))
    if now+1 <= n and not v[now+1]:
      v[now+1] = True
      d.append((now+1, cnt+1))
    if now-1 > 0 and not v[now-1]:
      v[now-1] = True
      d.append((now-1, cnt+1))  
  return dist[e]
        
n, m = map(int, input().split())
s, e = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, sys.stdin.readline().split())
  g[a].append(b)
  g[b].append(a)
v = [False] * (n+1)
dist = [1e9] * (n+1)
print(find(g, s, e, n, v, dist))
