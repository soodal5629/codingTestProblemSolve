from collections import deque
n, m = map(int, input().split())
d = [[] for _ in range(n)]
temp = input().split()
for i in range(n):
  d[i].append(int(temp[i]))
temp2 = input().split()
for i in range(n):
  if d[i][0] < int(temp2[i]):
    d[i].append(int(temp2[i]))
  else: d[i].append(-1)
d.sort(key = lambda x:(x[0], x[1]))
arr = deque(d)
while arr:
  s, back = arr.popleft()
  if back == -1 : continue
  if m < s: break
  m += (back - s)
print(m)
