n, m = map(int, input().split())
arr = [[0, 0]]
for i in range(m):
  arr.append(list(map(int, input().split())))
d = [[0 for _ in range(n+1)] for _ in range(m+1)]
for i in range(1, m+1):
  for j in range(1, n+1):
    day, page = arr[i]
    if day > j: d[i][j] = d[i-1][j]
    else:
      d[i][j] = max(d[i-1][j], page+d[i-1][j-day])
res = 0
for i in range(m+1):
  res = max(res, max(d[i]))
print(res)
