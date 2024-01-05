from collections import deque
def find(g, n , v, index):
  d = deque()
  d.append(index)
  while d:
    now = d.pop()
    v[now] = True
    for i in g[now]:
      if v[i] == False:
        d.append(i)
        v[now] = True
  return 1
  
t = int(input())
for k in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  g = [[] for _ in range(n+1)]
  for i in range(1, n+1):
    g[i].append(arr[i-1])
  v = [False] * (n+1)
  res = 0
  for i in range(1, n+1):
    if v[i] == False: res += find(g, n, v, i)
  print(res)
