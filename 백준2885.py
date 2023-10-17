import math
k = int(input())
a = n = 2 ** math.ceil(math.log2(k))
cnt = 0
temp = 0
if n == k: print(n, 0)
else:
  while temp != k:
    if temp + n <= k:
      temp += n
    else:
      cnt+=1
      n = n//2
  print(a, cnt)

