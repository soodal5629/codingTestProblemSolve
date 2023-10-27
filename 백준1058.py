from collections import deque, defaultdict

def dfs(d):
  arr = [0]*len(d)
  index= 0 
  m = 0
  while index < len(d):
    s = set()
    for j in d[index]:
      if index != j: s.add(j)
      for k in d[j]:
        if index!=k:
          s.add(k)
    m = max(m, len(s))
    index+=1
  return m

n = int(input())
d = defaultdict(list)
for i in range(n):
  s = input()
  for e,v in enumerate(s):
    if e!=i and v=='Y': d[i].append(e)
print(dfs(d))
