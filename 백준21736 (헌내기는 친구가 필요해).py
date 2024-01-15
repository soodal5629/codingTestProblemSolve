from collections import deque

def find(g, a, b, v,n, m):
  d = deque()
  d.append((a, b))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  cnt = 0
  while d:
    x, y = d.popleft()
    v[x][y] = True
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if g[nx][ny] != 'X' and v[nx][ny] == False:
          d.append((nx, ny))
          v[nx][ny] = True
          if g[nx][ny] == 'P': cnt+=1
  return cnt

n, m = map(int, input().split())
g = []
a = b = 0
for i in range(n):
  g.append(list(input()))
  if 'I' in g[i]:
    a = i
    b = g[i].index('I')
v = [[False for _ in range(m)]for _ in range(n)]
res = find(g, a, b, v, n, m)
if res == 0: res = 'TT'
print(res)
