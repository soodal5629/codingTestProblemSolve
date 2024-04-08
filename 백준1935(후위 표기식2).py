from collections import deque, defaultdict
n = int(input())
s = input()
dict = defaultdict(int)
temp = 65
for i in range(n):
  dict[chr(temp)] = int(input())
  temp+=1
d = deque()
res = 0
index = 0
for i in range(len(s)):
  if s[i].isalpha():
    d.append(s[i])
    continue
  b = d.pop()
  if b in dict: b= dict[b]
  a = d.pop()
  if a in dict: a= dict[a]
  if s[i] == '+':
    d.append(a+b)
  elif s[i] == '-':
    d.append(a-b)
  elif s[i] == '*':
    d.append(a*b)
  else:
    d.append(a/b)
print("{0:.2f}".format(d.pop()))
