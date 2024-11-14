from collections import deque
def find(r, c, g):
  d = deque()
  d.append(([[r, c]], 0, 0))
  res = 0
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  v = [[False for _ in range(5)] for _ in range(5)]
  while d:
    temp, dist, cnt = d.popleft()
    x, y = temp[-1]
    if g[x][y] == 1: cnt+=1
    if cnt >= 2 and len(temp)<=4:
      res = 1
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<5 and 0<=ny<5 and [nx, ny] not in temp:
        if g[nx][ny] != -1:
          temp2 = temp.copy()
          temp2.append([nx, ny])
          if len(temp2) > 4: continue
          d.append((temp2, dist+1, cnt))
  return res       

g = []
for i in range(5):
  g.append(list(map(int, input().split())))
r, c = map(int, input().split())
res = find(r, c, g)
print(res)
