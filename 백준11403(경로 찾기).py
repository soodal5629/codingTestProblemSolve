import copy
n = int(input())
g = []
for i in range(n):
  g.append(list(map(int, input().split())))
d = [[0 for _ in range(n)] for _ in range(n)]
d = copy.deepcopy(g)
for k in range(n):
  for i in range(n):
    for j in range(n):
      if d[i][k] == 1 and d[k][j] == 1:
        d[i][j] = 1
for i in range(n):
  for j in range(n):
    print(d[i][j], end=' ')
  print()
