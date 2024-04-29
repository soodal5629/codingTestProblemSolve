from collections import deque, defaultdict
def find(dict, a, b):
  res = 0
  d = deque()
  d.append(a)
  v = defaultdict(bool)
  v[a] = True
  while d:
    now = d.popleft()
    for i in dict[now]:
      if not v[i]:
        d.append(i)
        v[i] = True
  if v[a] and v[b]: return True
  else: return False

n = int(input())
dict = defaultdict(list)
a = b = ''
for i in range(n):
  a, b = map(str, input().split())
  if i < n-1: 
    dict[b].append(a)  
res = 0
if find(dict, a, b):
  res = 1
else:
  if find(dict, b, a):
    res = 1
print(res)
    
