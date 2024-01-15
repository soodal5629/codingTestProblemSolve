def change(g, x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      if g[i][j] == '1': g[i][j] = '0'
      else: g[i][j] = '1'
        
n, m = map(int, input().split())
a = []
b = []
for i in range(n):
  a.append(list(input()))
for i in range(n):
  b.append(list(input()))
res = 0

for i in range(n-2):
  for j in range(m-2):
    if a[i][j] != b[i][j]:
      res+=1
      change(a, i, j)

for i in range(n):
  for j in range(m):
    if a[i][j] != b[i][j]:
      res = -1
      break
print(res)
      
