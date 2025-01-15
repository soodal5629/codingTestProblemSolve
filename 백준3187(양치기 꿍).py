from collections import deque
def find(n, m, g, v, x, y):
  d = deque()
  d.append((x, y))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  s = f = 0
  v[x][y] = True
  while d:
    x, y = d.popleft()
    if g[x][y] == 'k':
      s+=1
    elif g[x][y] == 'v':
      f+=1
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and g[nx][ny] != '#' and not v[nx][ny]:
        v[nx][ny] = True
        d.append((nx, ny))
  if s > f: return [s, 0]
  else: return([0, f])
      
n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(input()))
v= [[False for _ in range(m)] for _ in range(n)]
s = f= 0 
for i in range(n):
  for j in range(m):
    if g[i][j] != '#' and not v[i][j]:
      res = find(n, m, g, v, i, j)
      s+=res[0]
      f+=res[1]
print(s, f)
