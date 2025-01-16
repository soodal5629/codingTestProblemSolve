from collections import deque
def find(n, g, v, x, y):
  dx = [1, 0]
  dy = [0, 1]
  temp = [['' for _ in range(n)] for _ in range(n)]
  res = -1
  for i in range(2):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0<=nx<n and 0<=ny<n and g[x][y] != g[nx][ny]:
      res = max(res, find2(n, x, y, nx, ny, g))
  return res
  
def find2(n, x, y, nx, ny, g):
  res= -1
  temp = [['' for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for  j in range(n):
      temp[i][j] = g[i][j]
  temp[x][y], temp[nx][ny] = temp[nx][ny], temp[x][y]
  c = [[1 for _ in range(n)] for _ in range(n)]
  c2 = [[1 for _ in range(n)] for _ in range(n)]
  # 가로
  for i in range(n):
    for j in range(1, n):
      if temp[i][j] == temp[i][j-1]:
        c[i][j] = max(c[i][j], c[i][j-1]+1)
    res = max(res, max(c[i]))
  
  # 세로
  for i in range(n):
    for j in range(1, n):
      if temp[j][i] == temp[j-1][i]:
        c2[j][i] = max(c2[j][i], c2[j-1][i]+1)
        res = max(res, c2[j][i])
  return res
        
n = int(input())
g = []
for i in range(n):
  g.append(list(input()))
v = [[False for _ in range(n)] for _ in range(n)]
res = -1
for i in range(n):
  for j in range(n):
    if not v[i][j]:
      res = max(res, find(n, g, v, i, j))
print(res)
