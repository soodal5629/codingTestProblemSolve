from collections import deque
def bfs(g, x, y, n, m):
  res = 0
  d = deque()
  d.append((x, y, 0))
  dx = [-1,1,0,0,-1,1,-1,1]
  dy = [0,0,-1,1,-1,1,1,-1]
  v = [[False for _ in range(m)] for _ in range(n)]
  while d:
    x, y, l = d.popleft()
    v[x][y] = True
    if g[x][y] == 1:
      return l
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not v[nx][ny]:
        d.append((nx, ny, l+1))
        v[nx][ny] = True
  return 0
n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
res = 0
for i in range(n):
  for j in range(m):
    res = max(res, bfs(g, i, j, n, m))
print(res)
