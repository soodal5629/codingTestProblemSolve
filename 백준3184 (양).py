from collections import deque
def bfs(g, x, y, o, visit, n , m):
  d = deque()
  d.append([x, y])
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  to = tv= 0
  while d:
    x, y = d.popleft()
    visit[x][y] = True
    if g[x][y] == 'o': to+=1
    elif g[x][y] == 'v': tv+=1
    for i in range(4):
      nowx = x+dx[i]
      nowy = y+dy[i]
      if 0<= nowx < n and 0 <= nowy < m:
        if visit[nowx][nowy]==False and g[nowx][nowy] != '#':
          visit[nowx][nowy] = True
          d.append([nowx, nowy])
  if to > tv: tv = 0
  else: to = 0
  return [to, tv]
          
n, m = map(int, input().split())
g = []
for i in range(n):
  g.append(list(input()))
visit = [[False for _ in range(m)] for _ in range(n)]
o = v = 0
for i in range(n):
  for j in range(m):
    if visit[i][j]==True or g[i][j] == '#': continue
    to, tv = bfs(g, i, j, o ,visit, n , m)
    o+=to
    v+=tv
print(o, v)
