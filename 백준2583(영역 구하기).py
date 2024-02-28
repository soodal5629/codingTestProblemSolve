from collections import deque
def dfs(g, v, x, y, n, m):
  d = deque()
  v[x][y] = True
  d.append((x, y))
  res = 0
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while d:
    x, y = d.pop()
    res+=1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and not v[nx][ny] and g[nx][ny] == 0:
        v[nx][ny] = True
        d.append((nx, ny))
  return res

n, m, k = map(int, input().split())
g = [[0 for _ in range(m)] for _ in range(n)]
for t in range(k):
  x, y, x2, y2 = map(int, input().split())
  for i in range(y, y2):
    for j in range(x, x2):
      g[i][j] = 1
cnt = 0
res = []
v = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
  for j in range(m):
    if not v[i][j] and g[i][j] == 0:
      res.append(dfs(g, v, i, j, n, m))
      cnt+=1
print(cnt)
res.sort()
for i in res:
  print(i, end=' ')
