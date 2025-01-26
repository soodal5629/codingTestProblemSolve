from collections import deque, defaultdict
n = int(input())
come = deque()
out = deque()
d = defaultdict()
for i in range(2*n):
  car = input()
  if i < n: come.append(car)
  else: out.append(car)
  d[car] = False
res = 0
x = y = 0
passed = [False] * (n)
while come:
  nowx = come.popleft()
  if d[nowx]: continue # 이미 지나간 차
  while out:
    nowy = out.popleft()
    if nowx != nowy:
      d[nowy] = True
      res+=1
    else:
      d[nowx] = True
      break
print(d)
print('res =', res)
