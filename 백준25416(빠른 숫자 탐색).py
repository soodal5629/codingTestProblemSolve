from collections import deque
def find(g, x, y):
  d = deque()
  d.append((x, y, 0))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  v = [[False for _ in range(5)] for _ in range(5)]
  v[x][y] = True
  while d:
    x, y, cnt = d.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<5 and 0<=ny<5 and not v[nx][ny]:
        if g[nx][ny] == 0:
          d.append((nx, ny, cnt+1))
          v[nx][ny] = True
        elif g[nx][ny] == 1:
          print(cnt+1)
          return cnt+1
  print(-1)
  return -1

g = []
for i in range(5):
  g.append(list(map(int, input().split())))
x, y = map(int, input().split())
find(g, x, y)
