from collections import deque
def find(g, x, v):
  d = deque()
  d.append(x)
  res = 0
  v[x] = True
  while d:
    now = d.popleft()
    res+=1
    for i in g[now]:
      if not v[i]:
        d.append(i)
        v[i] = True
  print(res-1)
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[b].append(a)
v = [False] * (n+1)
x = int(input())
find(g, x, v)
