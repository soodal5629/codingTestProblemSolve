from collections import deque
def find(g, x, y, v, n, m):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  d = deque()
  d.append((x, y))
  flag = False
  v[x][y]=True
  while d:
    x, y = d.popleft()
    if x == n-1: flag = True
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and not v[nx][ny] and g[nx][ny] == '0':
        v[nx][ny] = True
        d.append((nx, ny))
  if flag: return 1
  else: return 0

n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(input()))
cnt = 0
v = [[False for _ in range(m)]for _ in range(n)]
for j in range(m):
  if not v[0][j] and g[0][j] != '1': 
    cnt += find(g, 0, j, v, n, m)
if cnt > 0: print('YES')
else: print('NO')
