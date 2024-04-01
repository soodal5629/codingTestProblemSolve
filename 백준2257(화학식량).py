from collections import deque, defaultdict
dict = defaultdict(str)
dict['H'] = '1'
dict['C'] = '12'
dict['O'] = '16'
s = input()
d = deque()
n = len(s)
res = 0
index = temp = 0
for i, v in enumerate(s):
  if v in dict:
    if i > 0 and s[i-1] == ')' : d.append('+')
    d.append(dict[v])
    if i+1 <n:
      if s[i+1] in dict or s[i+1] == '(': d.append('+')
  elif v == ')':
    if i > 0 and s[i-1] == '(': d.append('0')
    d.append(v)
  elif v.isdigit():
    d.append('*' + v)
    if i+1 < n and s[i+1] in dict: d.append('+')
  else:
    d.append('+' + v)
print(eval(''.join(d)))
