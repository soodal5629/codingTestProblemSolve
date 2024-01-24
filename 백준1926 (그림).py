from collections import deque

def bfs(g, n, m, x, y, v):
  res = 1
  d = deque()
  d.append((x, y))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while d:
    x, y = d.popleft()
    v[x][y] = True
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and v[nx][ny] == False:
        if g[nx][ny] == 1:
          v[nx][ny] = True
          d.append((nx, ny))
          res+=1
  return res
n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
v = [[False for _ in range(m)] for _ in range(n)]

cnt = 0
width = 0
for i in range(n):
  for j in range(m):
    if not v[i][j] and g[i][j] == 1:
      cnt+=1
      width = max(width, bfs(g, n,m,i,j, v))

print(cnt)
print(width)
