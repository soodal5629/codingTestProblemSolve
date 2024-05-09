from collections import deque

def bfs(g, arr, dx, dy, x, y, v):
  res = 0
  d = deque()
  d.append((x, y))
  v[x][y] = True
  while d:
    x, y = d.popleft()
    res+=1
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<3 and 0<=ny<3 and not v[nx][ny] and g[nx][ny] == 'O':
        d.append((nx, ny))
        v[nx][ny] = True
  return res
n = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for t in range(n):
  g = []
  for i in range(3):
    g.append(list(input()))
  arr = list(map(int, input().split()))
  res = 1
  temp = []
  v = [[False for _ in range(3)] for _ in range(3)]
  for i in range(3):
    for j in range(3):
      if not v[i][j] and g[i][j] == 'O':
         temp.append(bfs(g, arr, dx, dy, i, j, v))
  arr = arr[1:]
  temp.sort()
  if len(arr) != len(temp):
    res = 0
  else:
    for i in range(len(arr)):
      if arr[i] != temp[i]:
        res = 0
        break
  print(res)
