from collections import deque
n, s, goal, f, b, k = map(int, input().split())
p = []
if k > 0: p = list(map(int, input().split()))
d = deque()
d.append((s, 0))
v = [False for _ in range(n+f+1)]
for i in p:
  v[i] = True
res = 1e9
while d:
  now, cnt = d.popleft()
  v[now] = True
  if now == goal:
    res = min(res, cnt)
    break
  x = now+f
  y = now-b
  if  0 < x <= n and not v[x]:
    v[x] = True
    d.append((x, cnt+1))
  if 0 < y <= n and not v[y]:
    v[y]=True
    d.append((y, cnt+1))
if res != 1e9: print(res)
else: print('BUG FOUND')
