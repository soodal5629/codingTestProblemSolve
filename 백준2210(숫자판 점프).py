from collections import deque
def find(g, x, y, temp):
  d = deque()
  d.append((x, y, str(g[x][y])))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  while d:
    x, y, s= d.popleft()
    if len(s) == 6:
      temp.add(s)
      continue
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<5 and 0<=ny<5:
        d.append((nx, ny, s+str(g[nx][ny])))
g = []
for i in range(5):
  g.append(list(map(int, input().split())))
temp = set()
for i in range(5):
  for j in range(5):
    find(g, i, j, temp)
print(len(temp))
