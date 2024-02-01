from collections import deque
def dfs(f, s, g, u, d):
  res = 1e9
  q = deque()
  if s == g: return 0
  q.append((s, 0))
  arr = []
  v = [1e9] * (f+1)
  v[s] = 0
  while q:
    now, cnt = q.popleft()
    if now == g:
      arr.append(cnt)
      #break
    if now+u <= f and v[now+u] > cnt+1:
      v[now+u] = cnt+1
      q.append((now+u, cnt+1))
    if now-d >= 1 and v[now-d] > cnt+1:
      v[now-d] = cnt+1
      q.append((now-d, cnt+1))
  if arr: res = min(arr)
  else: res = 'use the stairs'
  return res

f, s, g, u, d = map(int, input().split())
print(dfs(f, s, g, u, d))
