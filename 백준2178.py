from collections import deque
def find(arr):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  d = deque([])
  d.append([0, 0])
  n = len(arr)
  m = len(arr[0])
  v = [[False for _ in range(m)] for _ in range(n)]
  while d:
    x, y = d.popleft()
    v[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0  or nx >= n or ny < 0 or ny >= m or arr[nx][ny] == 0:
        continue
      if v[nx][ny] == False:
        arr[nx][ny] = arr[x][y] + 1
        d.append([nx, ny])
        v[nx][ny] = True # 얘가 있어야 시간초과 안됨 -> 없으면 무한루프 도는듯
      
  print(arr[n-1][m-1])
      
n, m = map(int, input().split())
arr = []
for i in range(n):
  temp = list(input())
  temp2= []
  for j in temp:
    temp2.append(int(j))
  arr.append(temp2)
find(arr)
