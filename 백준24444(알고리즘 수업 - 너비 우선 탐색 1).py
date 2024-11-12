from collections import deque
def find(n, m, start, g):
  v = [False] * (n+1)
  q = deque()
  q.append(start)
  v[start] = True
  res = [0] * (n+1)
  cnt = 1
  while q:
    now = q.popleft()
    res[now] = cnt
    cnt+=1
    g[now].sort()
    for i in g[now]:
      if not v[i]:
        v[i] = True
        q.append(i)
  for i in range(1, n+1):
    print(res[i])
      
    
n, m, r = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)
find(n, m, r, g)
