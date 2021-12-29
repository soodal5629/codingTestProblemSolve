n, e=map(int, input().split())
graph = [[1e9 for i in range(n+1)] for j in range(n+1)]
for i in range(n+1):
  for j in range(n+1):
    if i==j: graph[i][j] = 0
for i in range(e):
  a,b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] =1

x, k = map(int, input().split()) 
for i in range(1, n+1):
  for j in range(1, n+1):
    for k in range(1, n+1):
      if i==j : continue
      if graph[i][k]+graph[k][j]<graph[i][j]:
        graph[i][j] = graph[i][k]+graph[k][j]
for i in range(1, n+1):
  for j in range(1, n+1):
    print(graph[i][j], end=" ")
  print()
if graph[1][k]+graph[k][x]<1e9:
  print(graph[1][k]+graph[k][x])
else:
  print(-1)

