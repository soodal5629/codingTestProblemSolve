n = int(input())
h = [0]+list(map(int, input().split()))
joy = [0]+list(map(int, input().split()))
d = [[0 for _ in range(100)] for _ in range(n+1)]
for i in range(1, n+1):
  for j in range(1, 100):
    if h[i] > j: d[i][j] = d[i-1][j]
    else:
      d[i][j] = max(d[i-1][j], joy[i]+d[i-1][j-h[i]])
print(d[n][99])
