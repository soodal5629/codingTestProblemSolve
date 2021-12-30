# 다익스트라 풀이
import heapq

def dijkstra(start, graph, n):
  visit = [False] * (n+1)  
  cost = [1e9] * (n+1)
  cost[start] = 0 
  cnt = 0
  maxi = -1
  q = []
  heapq.heappush(q, (0, start))
  while q:
    c, start = heapq.heappop(q)
    if visit[start] == True: continue
    visit[start] = True
    for i in graph[start]:
      c, arrive = i
      if cost[start] + c < cost[arrive]:
        cost[arrive] = cost[start]+c
      if cost[arrive]>maxi: maxi = cost[arrive]
      heapq.heappush(q, (cost[arrive], arrive))
  for i in cost:
    if i == 1e9 or i==0: continue
    else: cnt+=1

  print(cnt, maxi)

n, e, c = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(e):
  a,b,cost = map(int, input().split())
  graph[a].append((cost, b))

dijkstra(c, graph, n)
