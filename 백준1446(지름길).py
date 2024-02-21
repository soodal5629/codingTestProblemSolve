import heapq
def find(q, dist, n, d):
  now = 0
  while q:
    s, e, l = heapq.heappop(q)
    if l < dist[e]:
      dist[e] = min(dist[e], dist[s] + l)
      temp = dist[e]+1
      for i in range(e+1, d+1):
        dist[i] = min(dist[i], temp)
        temp+=1
  print(dist[d])
  
n, d= map(int, input().split())
dist = [i for i in range(d+1)]
dist[0] = 0
q = []
for i in range(n):
  s, e, l = map(int, input().split())
  if e <= d and e-s > l:
    heapq.heappush(q, (s, e, l))
find(q, dist, n, d)
