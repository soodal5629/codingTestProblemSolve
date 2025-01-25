from collections import deque
def find(g, n, k):
  v = [False] * (n)
  d = deque()
  d.append(0)
  cnt = 0
  temp = -1
  while d:
    now = d.popleft()
    v[now] = True
    if now == k:
      temp = now
      break
    cnt+=1
    if not v[g[now]]:
      d.append(g[now])
  if temp == k: print(cnt)
  else: print(-1)
n, k = map(int, input().split())
g = [0] * (n)
for i in range(n):
  g[i] = int(input())
find(g, n, k)
