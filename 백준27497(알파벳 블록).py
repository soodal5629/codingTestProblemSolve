from collections import deque

t = int(input())
d = deque()
order = deque()

for k in range(t):
  arr = list(map(str, input().split()))
  n = w = ''
  if len(arr)>1: n, w = arr
  else: n = arr[0]
  
  if n == '1':
    d.append(w)
    order.append('R')
  elif n == '2':
    d.appendleft(w)
    order.append('L')
  else:
    if not d: continue
    temp = order.pop()
    if temp == 'R':
      d.pop()
    else:
      d.popleft()
if not d: print(0)
else: print(''.join(d))
