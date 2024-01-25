n, m = map(int, input().split())
g = [[1e9 for _ in range(n)] for _ in range(n)]
for i in range(n):
  g[i][i] = 0

for i in range(m):
  a, b = map(int, input().split())
  g[a-1][b-1] = 1
  g[b-1][a-1] = 1

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j: continue
      g[i][j] = min(g[i][k]+g[k][j], g[i][j])

arr = []
for i in range(n):
  arr.append([sum(g[i]), i+1])
arr.sort(key = lambda x:(x[0], x[1]))
print(arr[0][1])
