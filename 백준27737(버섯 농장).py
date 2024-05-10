from collections import deque
def find(g, x, y, v, k, dx, dy, n):
  v[x][y] = True
  d = deque()
  cnt = 0
  d.append((x, y))
  while d:
    x, y = d.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<n and not v[nx][ny] and g[nx][ny] == 0:
        cnt+=1
        if cnt >= k:
          return
        d.append((nx, ny))
        v[nx][ny] = True

n, m, k = map(int, input().split())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
v = [[False for _ in range(n)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0,-1,1]
cnt = 0
for i in range(n):
  for j in range(n):
    if not v[i][j] and g[i][j] == 0:
      find(g, i, j, v, k, dx, dy, n)
      cnt+=1
if cnt > m or cnt == 0:
  print('IMPOSSIBLE')
else:
  print('POSSIBLE')
  print(m-cnt)
