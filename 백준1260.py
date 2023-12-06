from collections import deque

def dfs(g, v, n, m):
  d = deque()
  d.append(v)
  visit = [False] * len(g)
  arr = []
  
  while d:
    now = d.pop()
    if visit[now]: continue
    arr.append(now)
    visit[now] = True
    temp = g[now]
    temp.sort(reverse = True)
    for i in temp:
      if visit[i] == False:
        d.append(i)
        
  for i in arr:
    print(i, end= ' ')

def bfs(g, v, n, m):
  d = deque()
  d.append(v)
  visit = [False] * len(g)
  arr = []
  visit[v] = True
  while d:
    now = d.popleft()
    arr.append(now)
    temp = g[now]
    temp.sort()
    for i in temp:
      if visit[i] == False:
        visit[i] = True
        d.append(i)
  for i in arr:
    print(i, end= ' ')
      
n, m, v = map(int, input().split())
g = [[] for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  g[a].append(b)
  g[b].append(a)

dfs(g, v, n+1, m+1)
print()
bfs(g, v, n+1, m+1)
