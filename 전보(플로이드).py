# 플로이드 워셜로 풀어버림..

n, e, c= map(int, input().split())
graph = [[1e9 for i in range(n+1)] for j in range(n+1)]
for i in range(1, n+1):
  for j in range(1, n+1):
    if i==j: graph[i][j] = 0 
for i in range(e):
  a,b,cost = map(int, input().split())
  graph[a][b] = cost
maxi = 0
cnt =0

for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      if i == j : continue
      if graph[i][k]+graph[k][j]<graph[i][j]:
        graph[i][j] = graph[i][k]+graph[k][j]
      
for i in range(1, n+1):
  if i == c: continue
  else:
    if graph[c][i] < 1e9:
      cnt+=1
      maxi = max(maxi, graph[c][i])
print(cnt, maxi)
