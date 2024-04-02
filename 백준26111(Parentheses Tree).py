from collections import deque
s = input()
res = 0
d = deque()
n= len(s)
i = 0
while i < n:
  if s[i] == '(':
    d.append(s[i])
    i+=1
  else:
    temp = -1e9
    while i<n and s[i] == ')' :
      top = d[-1]
      if top == '(':
        d.pop()
        if temp <= len(d):
          temp = len(d)
          res+=len(d)
        i+=1
print(res)      
