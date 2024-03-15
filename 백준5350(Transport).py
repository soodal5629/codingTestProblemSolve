t = int(input())
for k in range(t):
  n, w = map(int, input().split())
  arr = []
  for i in range(n):
    arr.append(list(map(int, input().split())))
  arr.sort(key = lambda x:(x[0], -x[1]))
  d = [[0 for _ in range(w+1)] for _ in range(n+1)]
  for i in range(n):
    weight, value = arr[i]
    for j in range(1, w+1):
      if weight > j:
        d[i][j] = d[i-1][j]
      else:
        d[i][j] = max(d[i-1][j], value+d[i-1][j-weight])
  print(d[n-1][w])
