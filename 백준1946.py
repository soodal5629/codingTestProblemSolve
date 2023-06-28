import sys

t = int(sys.stdin.readline())
for i in range(t):
  n = int(input())
  arr = []
  cnt = 1
  for j in range(n):
    a, b = list(map(int, sys.stdin.readline().split(' ')))
    arr.append([a, b])
  arr.sort(key = lambda x:x[0])
  my = arr[0][1]
  for j in range(1, n):
    x, y = arr[j]
    if my > y:
      cnt +=1
      my = y
  print(cnt)
