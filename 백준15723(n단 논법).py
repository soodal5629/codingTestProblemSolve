from collections import deque, defaultdict
def find(g, s):
  res = 'F'
  d = deque()
  a = s[0]
  b = s[-1]
  d.append(a)
  v = defaultdict(int)
  v[a] = 1
  while d:
    now = d.popleft()
    if now == b:
      res = 'T'
      break
    for i in g[now]:
      if v[i] == 0:
        d.append(i)
        v[i] = 1
  print(res)
  
n = int(input())
g = defaultdict(list)
for _ in range(n):
  s = input()
  g[s[0]].append(s[-1])
m = int(input())
for _ in range(m):
  s = input()
  find(g, s)
