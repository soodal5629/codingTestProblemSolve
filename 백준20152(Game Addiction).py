from collections import deque
h, n = map(int, input().split())
s = min(h, n)
e = max(h, n)
l = e - s 
g = [[1e9 for _ in range(l+1)] for _ in range(l+1)]
g[0][0] = 0
res = 0
if s == e: res = 1 
else:
  for i in range(l+1):
    for j in range(l+1):
      if i == 0 and j == 0: continue
      if j > i: continue
      if j == 0: g[i][j] = 1
      elif i == j: g[i][j] = g[i][j-1]
      else:
        g[i][j] = g[i-1][j] + g[i][j-1]
  res = g[l][l]
print(res)
