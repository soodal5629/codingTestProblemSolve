from collections import deque
def find(n, g, arr, r):
  d = deque()
  d.append(r)
  arr[r] = 0
  v = [False] * (n+1)
  while d:
    now = d.pop()
    v[now] = True
    g[now].sort(reverse=True)
    for x in g[now]:
      if not v[x]:
        d.append(x)
        arr[x] = arr[now]+1
  for i in range(1, n+1):
    print(arr[i])
n, m, r = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)
arr = [-1] * (n+1)
find(n, g, arr, r)
