from collections import deque
def find(g, n, m, x, y, v):
  d = deque()
  d.append((x, y))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  res = 0
  while d:
    x, y = d.popleft()
    v[x][y] = True
    res+=1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0<=nx<n and 0<=ny<m and g[nx][ny] == '.' and not v[nx][ny]:
        v[nx][ny] = True
        d.append((nx, ny))
  return res
  
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  g = []
  for i in range(n):
    g.append(list(input()))
  v= [[False for _ in range(m)] for _ in range(n)]
  cnt = 0
  temp = 0
  for i in range(n):
    for j in range(m):
      if g[i][j] == '.' and not v[i][j]:
        temp+=find(g, n, m, i, j, v)
        cnt+=1
  section = 'section'
  space = 'space'
  if cnt == 0 and temp == 0: print('0 sections, 0 spaces')
  else:
    if cnt > 1: section+='s'
    if temp > 1: space+='s'
    print('%d'%cnt, end=' ')
    print(section+', ', end='')
    print('%d'%temp, end=' ')
    print(space)
