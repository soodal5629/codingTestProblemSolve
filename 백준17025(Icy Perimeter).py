from collections import deque
def bfs(x, y, g, v):
  v[x][y] = True
  area = 0
  peri = 0
  d = deque()
  d.append((x, y))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while d:
    x, y = d.popleft()
    area+=1
    temp = 0
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<n and g[nx][ny]=='#':
        if not v[nx][ny]:
          v[nx][ny] = True
          d.append((nx, ny))
        temp+=1
    peri += (4-temp)
  return [area, peri]
n = int(input())
g = []
for i in range(n):
  g.append(list(input()))
area = peri = 0
v = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if g[i][j] == '#' and not v[i][j]:
      ta, tp = bfs(i, j, g, v)
      if ta > area:
        area = ta
        peri = tp
      elif ta == area:
        peri = min(peri, tp)
print(area, peri)
