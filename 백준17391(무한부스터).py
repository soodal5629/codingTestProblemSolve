from collections import deque
def find(g, n, m):
  d = deque()
  d.append((0, 0, 0))
  v = [[1e9 for _ in range(m)] for _ in range(n)]
  v[0][0] = 0
  while d:
    x, y, cnt = d.popleft()
    move = g[x][y]
    for i in range(x+1, x+move+1):
      if i >= n: break
      if v[i][y] > cnt+1:
        v[i][y] = cnt+1
        d.append((i, y, cnt+1))
    for j in range(y+1, y+move+1):
      if j >= m: break
      if v[x][j] > cnt+1:
        v[x][j] = cnt+1
        d.append((x, j, cnt+1))
  print(v[n-1][m-1])
n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
find(g, n, m)
