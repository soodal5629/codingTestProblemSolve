import sys
n, k = map(int, input().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
d = [[1e9 for _ in range(n)] for _ in range(2)]
d[0][0] = a[0]
d[1][0] = b[0]
for i in range(1, n):
  for j in range(2):
    if j == 0:
      if d[j+1][i-1] + k < d[j][i-1]:
        d[j][i] = d[j+1][i-1] + k + a[i]
      else: d[j][i] = d[j][i-1] + a[i]
    else:
      if d[j-1][i-1] + k < d[j][i-1]:
        d[j][i] = d[j-1][i-1] + k + b[i]
      else: d[j][i] = d[j][i-1] + b[i]
print(min(d[0][n-1], d[1][n-1]))
