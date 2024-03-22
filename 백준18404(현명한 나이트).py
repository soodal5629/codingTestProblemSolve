from collections import deque
def bfs(n, x, y, dist):
  dx = [-2, -2, -1, -1, 1, 1, 2, 2]
  dy = [-1, 1, -2, 2, -2, 2, -1, 1]
  d = deque()
  d.append((x, y, 0))
  v = [[False for _ in range(n)] for _ in range(n)]
  v[x][y] = True
  dist[x][y] = 0
  while d:
    x, y, cnt = d.popleft()
    for i in range(8):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < n and 0 <= ny < n and not v[nx][ny]:
        d.append((nx, ny, cnt+1))
        v[nx][ny] = True
        dist[nx][ny] = cnt+1
n, t =map(int,input().split())
x, y = map(int, input().split())
res = []
dist = [[1e9 for _ in range(n)] for _ in range(n)]
bfs(n, x-1, y-1, dist)  
for k in range(t):
  a, b= map(int, input().split())
  print(dist[a-1][b-1], end=' ')
