from collections import deque

s = input()
d = deque()
res = ''
arr = [' ', '<', '>']
index=  0
temp = ''
while index < len(s):
  v = s[index]
  if v not in arr:
    temp+=s[index]
    index+=1
  elif v == '<':
    res += temp[::-1]
    res += v
    index+=1
    while index < len(s):
      if s[index] == '>':
        res+=s[index]
        index+=1
        break
      res+=s[index]
      index+=1
    temp = ''
  elif v == ' ':
    res += (temp[::-1] + ' ')
    temp = ''
    index+=1
if temp!='': res+= temp[::-1]
print(res)
