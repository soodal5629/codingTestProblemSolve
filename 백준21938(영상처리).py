from collections import deque
def bfs(g, x, y, n, m, v):
  v[x][y] = True
  d = deque()
  d.append((x, y))
  dx = [0, 0, 1, -1]
  dy = [-1, 1, 0, 0]
  while d:
    x, y = d.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx< n and 0<=ny<m and not v[nx][ny] and g[nx][ny]==255:
        d.append((nx, ny))
        v[nx][ny] = True

n, m = map(int, input().split())
g = [[0 for _ in range(m)] for _ in range(n)]
temp = []
for i in range(n):
  temp.append(list(map(int, input().split())))
t = int(input())

for i in range(n):
  a = -1
  for j in range(0, m*3, 3):
    a = sum(temp[i][j:j+3])/3
    for k in range(0, m):
      if a >= t: g[i][j//3] = 255
res = 0
v = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
  for j in range(m):
    if not v[i][j] and g[i][j] == 255:
      res += 1
      bfs(g, i, j, n, m, v)
print(res)
