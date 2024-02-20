n, k = map(int, input().split())
s = [i for i in range(n, 0, -1)]
m = [i for i in range(1, n+1)]
d = [0] * n
if k == 0 or k==n: print(1)
else:
  temp = 1
  d1 = [0] * n
  d2 = [0] * n
  d = [0] * n
  for i in range(n):
    if i==0: 
      d1[i] = s[i]
      d2[i] = 1
      continue
    d1[i] = d1[i-1] * s[i]
    d2[i] = d2[i-1] * m[i]
  for i in range(n):
    d[i] = (d1[i] // d2[i]) % 10007
  print(d[k-1])
