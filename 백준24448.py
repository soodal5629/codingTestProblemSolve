from collections import deque
n = int(input())
d = deque()
res = []
for i in range(n):
  temp = input()
  if temp == 'READ':
    while d:
      read = d.pop()
      res.append(read)
      break
  else:
    d.append(temp)
for i in res:
  print(i)
