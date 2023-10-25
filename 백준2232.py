from collections import deque
n = int(input())
d = deque()
arr = []
for i in range(n):
  temp = int(input())
  d.append(temp)
  arr.append(0)
arr[0] = 1
m = d[0]
for i in range(1, n):
  if d[i] > d[i-1]:
    arr[i-1] = 0
    arr[i] = 1
  elif d[i] < d[i-1]:
    arr[i] = 0
  else:
    arr[i] = 1
for i in range(n):
  if arr[i] == 1:
    print(i+1)
