from collections import deque
def bfs(x, y, v, g, n, m):
  v[x][y] = True
  d = deque()
  d.append((x, y))
  dx = [1, -1, 0, 0, 1,-1, 1, -1]
  dy  =[0, 0, -1, 1, 1, -1,-1, 1]
  while d:
    x, y = d.popleft()
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < n and 0 <= ny<m and not v[nx][ny] and g[nx][ny] == '1':
        v[nx][ny] = True
        d.append((nx, ny))
  
n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(map(str, input().split())))
v = [[False for _ in range(m)] for _ in range(n)]
res = 0
for i in range(n):
  for j in range(m):
    if not v[i][j] and g[i][j] == '1':
      res+=1
      bfs(i,j,v,g,n,m)
print(res)
