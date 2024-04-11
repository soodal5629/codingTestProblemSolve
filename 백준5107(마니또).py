from collections import deque, defaultdict
def find(dict, key, v):
  d = deque()
  d.append(key)
  v[key] = True
  while d:
    now = d.popleft()
    if not v[dict[now]]:
      d.append(dict[now])
      v[dict[now]] = True
  
t = 1
while True:
  n = int(input())
  if n == 0: break
  dict = defaultdict(str)
  v = defaultdict(bool)
  for i in range(n):
    a, b = map(str, input().split())
    dict[a] = b
    v[a] = False
  cnt = 0
  for key in dict:
    if not v[key]:
      cnt+=1
      find(dict, key, v)
  print(t, cnt)
  t+=1
    
