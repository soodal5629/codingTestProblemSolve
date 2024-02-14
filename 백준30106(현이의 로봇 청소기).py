from collections import deque
def bfs(g, b, x, y, k, n , m):
  d = deque()
  d.append((x, y, g[x][y]))
  v[x][y] = True
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while d:
    x, y, h = d.popleft()
    for i in range(4):
      nx = x +dx[i]
      ny = y+dy[i]
      if 0 <= nx< n and 0<=ny<m:
        if abs(g[nx][ny] - h) <= k and not v[nx][ny]:
          v[nx][ny] = True
          d.append((nx, ny, g[nx][ny]))    
    
n, m , k = map(int, input().split())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
v = [[False for _ in range(m)] for _ in range(n)]
cnt = 0
for i in range(n):
  for j in range(m):
    if not v[i][j]: 
      cnt +=1
      bfs(g, v, i, j, k, n , m)
print(cnt)
