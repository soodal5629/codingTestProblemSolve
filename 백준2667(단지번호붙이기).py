from collections import deque
def bfs(j, x, y, v, n):
  d = deque()
  d.append((x, y, 1))
  res = 1
  dx = [-1, 1, 0 ,0]
  dy = [0, 0, -1, 1]
  while d:
    x, y, cnt = d.popleft()
    v[x][y] = True
    #res = max(res, cnt)
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<n and v[nx][ny] == False:
        if g[nx][ny] == '1':
          d.append((nx, ny, cnt+1))
          v[nx][ny] = True
          res+=1
  return res

n = int(input())
g = []
for i in range(n):
  g.append(list(input()))
v = [[False for _ in range(n)] for _ in range(n)]

cnt = 0
res = []
for i in range(n):
  for j in range(n):
    if not v[i][j] and g[i][j] != '0':
      cnt+=1
      res.append(bfs(g, i, j, v, n))
res.sort()
print(cnt)
for i in res:
  print(i)
