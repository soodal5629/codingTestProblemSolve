from collections import deque

def bfs(g, index, v):
  if v[index]: return 0
  d = deque()
  d.append(index)
  while d:
    now = d.popleft()
    v[now] = True
    for i in g[now]:
      if v[i]: continue
      v[i]= True
      d.append(i)
  return 1
    
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)
cnt = 0
v = [False] * (n+1)
for i in range(1, n+1):
  cnt += bfs(g, i, v)

print(cnt)
