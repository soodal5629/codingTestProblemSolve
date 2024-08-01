from collections import deque
def find(g, ax, ay, res, n, m, v):
  d = deque()
  d.append((ax, ay))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  v[ax][ay] = True
  while d:
    x, y = d.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < n and 0<=ny<m:
        if g[nx][ny] == 1 and not v[nx][ny]:
          d.append((nx, ny))
          v[nx][ny] = True
          res[nx][ny] = min(res[nx][ny], res[x][y]+1)
n, m = map(int, input().split())
g = []
ax = ay = -1
for i in range(n):
  g.append(list(map(int, input().split())))
  if g[i].count(2) == 1:
    ax = i
    ay = g[i].index(2)
res = [[1e9 for _ in range(m)] for _ in range(n)]
res[ax][ay] = 0
v = [[False for _ in range(m)] for _ in range(n)]
find(g, ax, ay, res, n, m, v)
for i in range(n):
  for j in range(m):
    if g[i][j] == 0: res[i][j] = 0
    elif res[i][j] ==1e9: res[i][j] = -1
  
for i in range(n):
  for j in range(m):
    print(res[i][j], end = ' ')
  print()
