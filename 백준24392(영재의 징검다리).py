n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.insert(0, list(map(int, input().split())))
d = [[0 for _ in range(m)] for _ in range(n)]
for i in range(m):
  d[0][i] = arr[0][i]
for i in range(1, n):
  for j in range(m):
    if arr[i][j] == 0: continue
    if arr[i-1][j] == 1: d[i][j]+=d[i-1][j]
    if j-1 >= 0 and arr[i-1][j-1] == 1: d[i][j]+=d[i-1][j-1]
    if j+1 < m and arr[i-1][j+1] == 1: d[i][j]+=d[i-1][j+1]
print(sum(d[n-1])%1000000007)
