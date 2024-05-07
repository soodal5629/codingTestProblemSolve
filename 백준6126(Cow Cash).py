v, n = map(int, input().split())
c = [0]
for i in range(v):
  c.append(int(input()))
c.sort()
d = [[0 for _ in range(n+1)] for _ in range(v+1)]

for i in range(1, v+1):
  for j in range(1, n+1):
    if i == 1:
      if j >= c[i]:
        if j%c[i] == 0: d[i][j] = 1            
    else:
      temp = d[i-1][j]
      cnt = 1
      while c[i]*cnt <= j:
        temp += d[i-1][j-c[i]*cnt]
        if j-c[i]*cnt == 0: temp+=1
        cnt+=1
      d[i][j] = temp 
print(d[v][n])
