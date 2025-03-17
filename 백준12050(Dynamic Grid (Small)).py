from collections import deque

def find(g, n, m, x, y,v):
  d = deque()
  d.append((x, y))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  while d:
    x, y = d.popleft()
    v[x][y] = True
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and g[nx][ny] == '1' and not v[nx][ny]:
        v[nx][ny] = True
        d.append((nx, ny))

t = int(input())
num = 0
for _ in range(t):
  num+=1
  n, m = map(int, input().split())
  g = []
  for i in range(n):
    g.append(list(input()))
  z = int(input())
  arr = []
  for a in range(z):
    s = input()
    v = [[False for _ in range(m)] for _ in range(n)]
    if s == 'Q':
      temp = 0
      for i in range(n):
        for j in range(m):
          if g[i][j] == '1' and not v[i][j]:
            find(g, n, m, i, j,v)
            temp+=1
      arr.append(temp)
    else:
      start, tx, ty, value = s.split()
      tx = int(tx)
      ty = int(ty)
      g[tx][ty] = value
  print('Case #%d:' %num)
  for i in arr:
    print(i)
