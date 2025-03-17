from collections import deque
n, m = map(int, input().split())
g = []
g.append(['.' for _ in range(m+2)])
for i in range(n):
  g.append(['.']+list(input())+['.'])
g.append(['.' for _ in range(m+2)])
arr = []
for i in range(n+2):
  for j in range(m+2):
    if g[i][j] == 'X':
      cnt = 0
      dx = [-1, 1, 0, 0]
      dy = [0, 0, -1, 1]
      for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]
        if g[nx][ny] == '.':
          cnt +=1        
      if cnt >=3:
        g[i][j] = 'T'
      else:  arr.append((i, j))
if len(arr) == 1: print('X')
else:
  x1 = 11
  x2 = -1
  y1 = 11
  y2 = -1
  for v in arr:
    x, y = v
    x1 = min(x1, x)
    x2 = max(x2, x)
    y1 = min(y1, y)
    y2 = max(y2, y)
  for i in range(x1, x2+1):
    for j in range(y1, y2+1):
      if g[i][j] == 'T': g[i][j] = '.'
      print(g[i][j], end='')
    print()
