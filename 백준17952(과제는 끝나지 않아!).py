from collections import deque
n = int(input())
d = deque()
res = 0
for i in range(n):
  arr = list(map(int, input().split()))
  if len(arr) == 1:
    if not d: continue
    else:
      top_a, top_t = d.pop()
      if top_t-1 > 0 :
        d.append((top_a, top_t-1))
      else:
        res+=top_a
    continue
  o, a, t = arr  
  if not d:
    if t-1 > 0:
      d.append((a, t-1))
    else:
      res+=a
    continue
  else:
    if t-1 > 0:
      d.append((a, t-1))
    else:
      res+=a
print(res)
