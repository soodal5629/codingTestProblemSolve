n, m = map(int, input().split())
g = []
v = [[False for _ in range(m)] for _ in range(n)]
for i in range(n):
  g.append(list(map(int, input().split())))
for i in range(n):
  for j in range(m):
    if i== 0 and j==0: continue
    elif i == 0: g[i][j] += g[i][j-1]
    elif j == 0: g[i][j] += g[i-1][j]
    else:
      g[i][j] += max(g[i-1][j], g[i][j-1])
print(g[n-1][m-1])
