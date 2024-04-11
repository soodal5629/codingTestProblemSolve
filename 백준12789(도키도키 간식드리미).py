from collections import deque
n = int(input())
arr = list(map(int, input().split()))
d = deque()
now = 1
for i in range(n):
  v = arr[i]
  if now == v:
    now+=1
    while d:
      temp = d.pop()
      if temp == now:
        now+=1
      else: 
        d.append(temp)
        break
  else:
    d.append(v)
if d: print('Sad')
else: print('Nice')
