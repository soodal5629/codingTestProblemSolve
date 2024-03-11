from collections import deque
def find(n, a, b, m):
  v = [1e9] * 100001
  v[n] = 0
  d = deque()
  d.append(n)
  while d:  
    now = d.popleft()
    if now+1<=100000 and v[now+1] > v[now]+1:
      v[now+1] = v[now]+1
      d.append(now+1)
    if now-1 >=0 and v[now-1] > v[now]+1:
      v[now-1] = v[now]+1
      d.append(now-1)
    if now*a <= 100000 and v[now*a] > v[now]+1:
      v[now*a] = v[now]+1
      d.append(now*a)
    if now*b <= 100000 and v[now*b] > v[now]+1:
      v[now*b] = v[now]+1
      d.append(now*b)
    if now+a<=100000 and v[now+a] > v[now]+1:
      v[now+a] = v[now]+1
      d.append(now+a)
    if now-a >=0 and v[now-a] > v[now]+1:
      v[now-a] = v[now]+1
      d.append(now-a)
    if now+b<=100000 and v[now+b] > v[now]+1:
      v[now+b] = v[now]+1
      d.append(now+b)
    if now-b >=0 and v[now-b] > v[now]+1:
      v[now-b] = v[now]+1
      d.append(now-b)
  print(v[m])
      
a, b, n, m = map(int, input().split())
find(n, a, b, m)
