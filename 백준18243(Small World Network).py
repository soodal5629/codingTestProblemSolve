from collections import deque
def find(g, x, n, m):
  d = deque()
  v = [1e9] * (n+1)
  v[x] = 0
  d.append(x)
  while d:
    x = d.popleft()
    for i in g[x]:
      if v[i] > v[x] + 1:
        v[i] = v[x] + 1
        d.append(i)
  for i in range(1, n+1):
    if v[i] > 6:
      return False
  return True
        
n, m = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)
flag  = True
for i in range(1, n+1):
  flag = find(g, i, n, m)
if flag: print('Small World!')
else: print('Big World!')
