from collections import deque
def dfs(n, k, arr,v):
  d = deque()
  d.append((n, 0))
  v[n] = 0
  while d:
    n, cnt = d.popleft()
    if n == k:
      arr.append(cnt)
      break
    else:
      if 0< n*2 <= k+1 and v[n*2] > cnt+1:
        d.append((n*2, cnt+1))
        v[n*2] = cnt+1
      if n+1 <= k+1 and v[n+1] > cnt+1:
        d.append((n+1, cnt+1))
        v[n+1] = cnt+1
      if n-1>=0 and v[n-1] > cnt+1:
        d.append((n-1, cnt+1))   
        v[n-1] = cnt+1
  
n, k = map(int, input().split())
arr = []
v = [1e9] * (100001)
dfs(n, k, arr, v)
print(arr[0])
