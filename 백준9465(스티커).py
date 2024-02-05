t = int(input())
for k in range(t):
  n = int(input())
  arr = []
  for i in range(2):
    arr.append(list(map(int, input().split())))
  d = [[0 for _ in range(n)] for _ in range(2)]
  for j in range(n):
    for i in range(2):
      if j == 0:
        d[i][j] = arr[i][j]
      elif j == 1:
        if i == 0: d[i][j] = arr[i][j] + d[1][j-1]
        else: d[i][j] = arr[i][j] + d[0][j-1]
      else:
        temp = 0
        if i == 0: temp = d[1][j-1]
        else: temp = d[0][j-1]
        d[i][j] = arr[i][j] + max(temp, d[0][j-2], d[1][j-2])
  m = -1
  for i in range(2):
    m = max(m, max(d[i]))
  print(m)
