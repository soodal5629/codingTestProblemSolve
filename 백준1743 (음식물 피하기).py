from collections import deque
def bfs(g, n, m, x, y, v):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  d = deque()
  d.append((x, y))
  cnt = 0
  while d:
    x, y = d.popleft()
    v[x][y] = True
    cnt+=1
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < n and 0<=ny<m:
        if v[nx][ny] == False and g[nx][ny] == 1:
          v[nx][ny] = True
          d.append((nx, ny))
  return cnt   
n, m, k = map(int, input().split())
g = [[0 for _ in range(m)] for _ in range(n)]
for i in range(k):
  x, y = map(int, input().split())
  g[x-1][y-1] = 1
v = [[False for _ in range(m)] for _ in range(n)]

res = 0
for i in range(n):
  for j in range(m):
    if v[i][j] or g[i][j] == 0: continue
    temp = bfs(g, n, m, i, j, v)
    res = max(res, temp)
print(res)
