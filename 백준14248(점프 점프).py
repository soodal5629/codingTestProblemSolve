from collections import deque
def find(n, arr,s, v):
  res = 1
  d = deque()
  d.append((s-1, 0))
  v[s-1] = True
  while d:
    now, cnt = d.popleft()
    j = arr[now]
    if now-j >= 0 and not v[now-j]:
      v[now-j] = True
      d.append((now-j, cnt+1))
    if now+j < n and not v[now+j]:
     v[now+j] = True
     d.append((now+j, cnt+1))
  return v.count(True)
        
n = int(input())
arr = list(map(int, input().split()))
s = int(input())
v = [False] * n  
print(find(n, arr, s, v))
