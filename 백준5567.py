from collections import deque
def bfs(g, n):
  v = [False] * (n+1)
  v[1] = True
  d = deque()
  d.append((1, 0))
  res = 0
  while d:
    now, cnt = d.popleft()
    for i in g[now]:
      if v[i]==False:
        d.append((i, cnt+1))
        v[i] = True
        if cnt+1 < 3: res+=1
  return res    

n = int(input())
m = int(input())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)
print(bfs(g, n))
