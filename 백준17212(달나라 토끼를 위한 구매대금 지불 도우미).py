n = int(input())
m = [1, 2, 5, 7]
d = [1e9] * (100001)
if n == 0:
  print(0)
else:  
  for i in m:
    d[i] = 1
  for i in range(1, n+1):
    for j in range(len(m)):
      if m[j] > i: continue
      if i % m[j] == 0:
        d[i] = min(d[i], i//m[j])
      d[i] = min(d[i], 1+d[i-m[j]])
  print(d[n])
