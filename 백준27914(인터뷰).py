import copy
n, k, q = map(int, input().split())
arr = list(map(int, input().split()))
question = list(map(int, input().split()))
d = [1] * n
for i in range(n):
  if arr[i] == k:
    d[i] = 0
for i in range(1, n):
  if arr[i] == k or arr[i-1] == k: continue
  d[i] += d[i-1]
d2 = copy.deepcopy(d)
for i in range(1, n):
  d2[i] += d2[i-1]
for i in question:
  print(d2[i-1])
