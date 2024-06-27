from collections import deque
def find(g, x, y, v, n, m):
  d = deque()
  d.append((x, y))
  dx = [-1, 1, 0, 0, 1, -1, 1, -1]
  dy = [0, 0, -1, 1, 1, -1, -1, 1]
  v[x][y] = True
  while d:
    x, y = d.popleft()
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m:
        if not v[nx][ny] and g[nx][ny] == '@':
          v[nx][ny] = True
          d.append((nx, ny))
          
while True:
  n, m = map(int, input().split())
  if n == m == 0: break
  g = []
  for i in range(n):
    g.append(list(input()))
  v = [[False for _ in range(m)] for _ in range(n)]
  res = 0
  for i in range(n):
    for j in range(m):
      if not v[i][j] and g[i][j] == '@':
        res+=1
        find(g, i, j, v, n, m)
  print(res)
