from collections import deque

t = int(input())
for _ in range(t):
  n, index = map(int, input().split())
  arr = deque(list(map(int, input().split())))
  d = deque()
  for i in range(len(arr)):
    d.append((i, arr[i]))
  cnt = 0
  v = arr[index]
  while d:
    x, now = d.popleft()
    flag = False
    for i in range(len(d)):
      if d[i][1] > now:
        d.append((x, now))
        flag = True
        break
    if not flag:
      cnt+=1
      if now == v and x == index:
        break
  print(cnt)
