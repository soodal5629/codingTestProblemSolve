from collections import deque
def find(arr, s, n, m):
  d = deque()
  d.append((s, 1))
  temp = [0]
  v = [False] * (n+1)
  while d:
    now, cnt = d.pop()
    if now not in temp: temp.append(now)
    v[now] = True
    g[now].sort()
    for i in g[now]:
      if not v[i]:
        d.append((i, arr[now]+1))
  for i in range(1, len(temp)):
    arr[temp[i]]=i
  for i in range(1, n+1):
    print(arr[i])

n, m, r = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)
arr = [0] * (n+1)
arr[r] = 1
find(arr, r, n, m)
