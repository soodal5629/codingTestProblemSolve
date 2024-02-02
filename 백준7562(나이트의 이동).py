from collections import deque
def bfs(n, x, y, a, b):
  d = deque()
  d.append((x, y, 0))
  v = [[False for _ in range(n)] for _ in range(n)]
  dx = [-2, 2, -2, 2, 1, 1, -1, -1]
  dy = [1, 1, -1, -1, -2, 2, -2, 2]
  res = 0
  while d:
    x, y, cnt = d.popleft()
    v[x][y] = True
    if x == a and y == b:
      res = cnt
      break
    for i in range(8):
      nx = dx[i]+x
      ny = dy[i]+y
      if 0<=nx<n and 0<=ny<n and not v[nx][ny]:
        v[nx][ny] = True
        d.append((nx, ny, cnt+1))
  return res

t = int(input())
for k in range(t):
  n = int(input())
  x, y = map(int, input().split())
  a, b = map(int, input().split())
  print(bfs(n, x, y, a,b))
