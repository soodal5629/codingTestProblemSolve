from collections import deque
s = input()
d = deque()
index = 0
n = len(s)
while index < n:
  if not d:
    d.append(s[index])
    index+=1
    continue
  top = d[-1]
  now = s[index]
  if top == now or (top == ')' and now == '('):
    d.append(s[index])
    index+=1
  else:
    while index < n and d:
      top = d[-1]
      now = s[index]
      if top == '(' and now == ')':
        d.pop()
        index+=1
      else:
        break
print(len(d))
