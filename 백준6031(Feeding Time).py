from collections import deque
def find(g, n, m, x, y, v):
  d = deque()
  cnt = 0
  d.append((x, y))
  dx = [-1, 1, 0, 0, 1, -1, -1, 1]
  dy = [0, 0, -1, 1, 1, -1, 1, -1]
  while d:
    x, y = d.popleft()
    v[x][y] = True
    cnt+=1
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and g[nx][ny] == '.' and not v[nx][ny]:
        d.append((nx, ny))
        v[nx][ny] = True
  return cnt

m, n = map(int, input().split())
g = []
for i in range(n):
  g.append(list(input()))
res = 0
v = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
  for j in range(m):
    if g[i][j]=='.' and not v[i][j]:
      res = max(res, find(g, n, m, i, j, v))
print(res)
