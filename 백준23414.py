from collections import deque
s = input()
t = deque(input())
d = deque()
index = 0
while t:
  now = t[0]
  if index < len(s) and now == s[index]:
    d.append(t.popleft())
    index+=1
  else:
    if len(t) >= 2:
      t.popleft()
      t.popleft()
    else:
      d.append(t.popleft())
if t:
  for i in t: d.append(i)
if ''.join(d) == s:
  print('YES')
else: print('NO')
