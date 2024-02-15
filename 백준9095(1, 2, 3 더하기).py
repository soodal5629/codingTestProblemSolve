from collections import deque
def find(n):
  d = deque([1, 2, 3])
  cnt = 0
  while d:
    now = d.popleft()
    if now == n:
      cnt+=1
    if now + 1 <= n: d.append(now+1)
    if now + 2 <= n: d.append(now+2)
    if now + 3 <= n: d.append(now+3)
  return cnt
t = int(input())
for k in range(t):
  n = int(input())
  res = find(n)
  print(res)
