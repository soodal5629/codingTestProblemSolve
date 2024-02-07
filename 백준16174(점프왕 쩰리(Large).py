from collections import deque
def bfs(g, n):
  d = deque()
  d.append((0, 0, g[0][0]))
  v = [[False for _ in range(n)] for _ in range(n)]
  v[0][0] = True
  while d:
    x, y, j = d.popleft()
    if x == n-1 and y == n-1:
      return 'HaruHaru'
    nx = x+j
    ny = y+j
    if nx < n:
      if not v[nx][y]:
        v[nx][y] = True
        d.append((nx, y, g[nx][y]))
    if ny <n:
      if not v[x][ny]:
        v[x][ny] = True
        d.append((x, ny, g[x][ny]))
  return 'Hing'    
n = int(input())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
print(bfs(g, n))
