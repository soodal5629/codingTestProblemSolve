import heapq
from collections import deque
n = int(input())
q = []
res = 0
arr = []
for i in range(n):
  a, start, end = list(map(int, input().split()))
  arr.append([start, end])
arr.sort(key = lambda x:x[0])
arr = deque(arr)

while arr:
  start, end = arr.popleft()
  if len(q) == 0:
    res+=1
    heapq.heappush(q, [end, start])
    continue
  
  comp_e, comp_s =heapq.heappop(q)
  if start < comp_e and start >= comp_s:
    heapq.heappush(q, [end, start])
    heapq.heappush(q, [comp_e, comp_s])
    res+=1
  else:
    heapq.heappush(q, [end, start])

print(res)
