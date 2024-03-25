from collections import deque
s= input()
d = deque()
n = len(s)
res = 0
for i in range(n):
  if s[i].isdigit():
    d.append(int(s[i]))
  else:
    sec = d.pop()
    fir = d.pop()
    if s[i] == '*':
      d.append(fir * sec)
    elif s[i] == '+':
      d.append(fir + sec)
    elif s[i] == '-':
      d.append(fir - sec)
    elif s[i] == '/':
      d.append(fir // sec)
print(d.popleft())
