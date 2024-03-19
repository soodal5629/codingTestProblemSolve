n = int(input())
arr = list(map(int, input().split()))
k = int(input())
d = [1e9] * 1001
d[0] = 0
d[1] = 1
for i in arr:
  d[i] = 1
for i in range(2, 1001):
  for j in arr:
    if i%j == 0:
        d[i] = min(d[i], i//j)
    d[i] = min(d[i], d[i-j]+1)
  if d[i] > k:
    if i%2 == 0: 
      print('holsoon win at', i)
    else:
     print('jjaksoon win at', i)
    break
