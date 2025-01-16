from collections import deque
def find(n,m,g,v,x, y):
  d = deque()
  d.append((x, y))
  dx= [-1, 1, 0, 0]
  dy = [0, 0,-1, 1]
  while d:
    x, y= d.popleft()
    v[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and not v[nx][ny] and g[nx][ny] == '#':
        v[nx][ny] = True
        d.append((nx, ny))
    
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  g = []
  for i in range(n):
    g.append(list(input()))
  v = [[False for _ in range(m)] for _ in range(n)]
  res = 0
  for i in range(n):
    for j in range(m):
      if not v[i][j] and g[i][j] == '#':
        find(n,m,g,v,i,j)
        res+=1
  print(res)
