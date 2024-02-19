from collections import deque
def bfs(a, b, a2, b2, v, n):
  d = deque()
  d.append((a, b, 0))
  dx = [-2, -2, 0, 0, 2, 2]
  dy = [-1, 1, -2, 2, -1, 1]
  v[a][b] = True
  while d:
    x, y, cnt = d.popleft()
    if x == a2 and y == b2:
      return cnt
    for i in range(6):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<n and not v[nx][ny]:
        v[nx][ny] = True
        d.append((nx, ny, cnt+1))
  return -1
        
n = int(input())
a1, b1, a2, b2 = map(int, input().split())
v = [[False for _ in range(n)] for _ in range(n)]
res = bfs(a1, b1, a2, b2, v, n)
print(res)
