from collections import deque, defaultdict
def find(n, m, p, g):
  d = deque()
  d.append(p)
  cnt = 0
  while d:
    p = d.popleft()
    if cnt > n:
      cnt = -1
      break
    fav, hate = g[dict[p]]
    if p == hate:
      cnt+=1
      d.append(fav)   
  print(cnt)

n, m, p = map(int, input().split())
g = [[] for _ in range(n+1)]
g[0] = [-1, -1]
dict = defaultdict(int)
for i in range(n):
  a, b = map(int, input().split())
  g[i+1].append(a)
  g[i+1].append(b)
  if dict[b] == 0: dict[b] = i+1
find(n, m, p, g)
