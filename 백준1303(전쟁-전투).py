from collections import deque
def bfs(g, n, m, x, y, word, v):
  res = 0
  d = deque()
  d.append([x, y])
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while d:
    x, y = d.popleft()
    v[x][y] = True
    res+=1
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < n and 0<=ny<m:
        if not v[nx][ny] and g[nx][ny] == word:
          d.append([nx, ny])
          v[nx][ny] = True
  return res**2 
  
n, m = map(int, input().split())
n, m = m, n # 문제 잘 읽어야 함
g = []
for i in range(n):
  g.append(list(input()))
v = [[False for _ in range(m)]for _ in range(n)]
w = b = 0
for i in range(n):
  for j in range(m):
    if not v[i][j]:
      res = bfs(g, n, m, i, j, g[i][j], v)
      if g[i][j] == 'W': w+= res
      else: b+=res
print(w, b)
