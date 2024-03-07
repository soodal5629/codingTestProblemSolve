from collections import deque
def find(g, n, a, b):
  res = 1e9
  d = deque()
  d.append(a)
  v = [False] * (10001)
  v[a] = True
  dist = [1e9] * 10001
  dist[a] = 0
  while d:
    index = d.popleft()
    if index == b: break
    now = g[index]
    for i in range(1, n+1):
      if abs(index-i) % now == 0 and not v[i]:
        d.append(i)
        dist[i] = min(dist[i], dist[index]+1)
        v[i] = True
  if dist[b] == 1e9: print(-1)
  else: print(dist[b])

n = int(input())
temp = list(map(int, input().split()))
g = [0] + temp
a, b= map(int, input().split())
find(g, n, a, b)
