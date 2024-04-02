from collections import deque
def find(g, n, dist):
  d = deque()
  d.append(1)
  v=[False] * (n+1)
  v[1] = True
  while d:
    now = d.popleft()
    g[now].sort(key = lambda x:-x[1])
    for i in g[now]:
      x, l = i
      if not v[x] and dist[x] < l:
        d.append(x)
        v[x] = True
        dist[x] = dist[now] + l
  print(max(dist))
  
n = int(input())
g = [[] for _ in range(n+1)]
dist = [-1e9] * (n+1)
dist[0] = 0
dist[1] = 0
for i in range(n-1):
  a, b, c = map(int, input().split())
  g[a].append([b, c])
  g[b].append([a, c])
find(g, n, dist)
