from collections import deque

def bfs(g, w, h, x, y, v):
  if g[x][y] == 0 or v[x][y] == True: return 0
  d = deque()
  d.append((x, y))
  dx = [-1, 1, 0, 0, 1, -1, -1, 1]
  dy = [0, 0, -1, 1, 1, -1, 1, -1]
  while d:
    x, y = d.popleft()
    v[x][y] = True
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < h and 0 <= ny < w:
        if v[nx][ny] == False and g[x][y] == 1:
          v[nx][ny] = True
          d.append((nx, ny))
  return(1)
  
w, h = map(int, input().split())
while w != 0 and h != 0:
  arr = []
  for i in range(h):
    arr.append(list(map(int, input().split())))
  cnt = 0
  v = [[False for _ in range(w)] for _ in range(h)]
  for i in range(h):
    for j in range(w):
      cnt += bfs(arr, w, h, i, j, v)  
  print(cnt)
  w, h = map(int, input().split())


  
