from collections import deque
def find(a, b):
  d = deque()
  d.append((a, 0, b))
  res = 1e9
  while d:
    now, cnt, target = d.popleft()
    if now == target:
      res = min(res, cnt)
      break
    if now + 1 <= target:
      d.append((now+1, cnt+1, target))
    if now + now <= target+3:
      d.append((now+now, cnt+1, target+3))
  print(res)
      
t = int(input())
for k in range(t):
  a, b = map(int, input().split())
  find(a, b)
