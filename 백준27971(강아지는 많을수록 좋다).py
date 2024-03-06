from collections import deque, defaultdict
def find(n, a, b, s):
  d = deque()
  d.append((0, 0))
  dict = defaultdict(int)
  while d:
    now, cnt = d.popleft()
    if now > n: continue
    dict[now]+=1
    if now == n:
      print(cnt)
      return
    if dict[now+a] == 0 and now+a not in s:
      d.append((now+a, cnt+1))
      dict[now+a]+=1
    if dict[now+b] == 0 and now+b not in s:
      d.append((now+b, cnt+1))
      dict[now+b]+=1
  print(-1)

n, t, a, b = map(int, input().split())
s = set()
for i in range(t):
  temp1, temp2 = map(int, input().split())
  for j in range(temp1, temp2+1):
    s.add(j)
find(n, a, b, s)
