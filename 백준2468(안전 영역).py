from collections import deque
import copy

def find(g, h, n, x, y, v):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  d = deque()
  d.append((x, y))
  v[x][y] = True
  while d:
    x, y = d.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<n and not v[nx][ny] and g[nx][ny]>h:
        d.append((nx, ny))
        v[nx][ny] = True
  return 1
  
n = int(input())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
maxi = -1
for i in g:
  maxi = max(maxi,max(i))
res = 1
for h in range(1, maxi+1):
  v = [[False for _ in range(n)] for _ in range(n)]
  temp = 0
  for i in range(n):
    for j in range(n):
      if g[i][j] > h and not v[i][j]: 
        find(g, h, n, i, j, v)
        temp+=1
  res = max(res, temp)
print(res)
