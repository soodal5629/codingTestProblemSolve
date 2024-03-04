from collections import deque
import copy
def find(g, n, m, k):
  d = deque()
  d.append((n-1, 0, 1, [[n-1, 0]]))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  res = 0
  while d:
    x, y, cnt, arr = d.popleft()
    if x == 0 and y == m-1:
      if cnt == k: res+=1
      continue
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<n and 0<=ny<m and g[nx][ny] != 'T' and [nx, ny] not in arr:
          temp = copy.deepcopy(arr)
          temp.append([nx, ny])
          d.append((nx, ny, cnt+1, temp))
  return res
        
n, m, k = map(int, input().split())
g = []
for i in range(n):
  g.append(list(input()))
res = find(g, n, m, k)
print(res)
