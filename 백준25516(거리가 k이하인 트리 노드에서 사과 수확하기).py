from collections import deque
def find(n, k, g, apple):
  res = 0
  d = deque()
  d.append((0, 0))
  v = [False] * (n)
  v[0] = True
  while d:
    now, cnt = d.popleft()
    if apple[now] == 1:
      res+=1
    for i in g[now]:
      if not v[i] and cnt+1 <= k:
        v[i] = True
        d.append((i, cnt+1))
  return res
    
n, k = map(int, input().split())
g = [[] for _ in range(n)]
for i in range(n-1):
  a, b= map(int, input().split())
  g[a].append(b)
apple = list(map(int, input().split()))
print(find(n, k, g, apple))
