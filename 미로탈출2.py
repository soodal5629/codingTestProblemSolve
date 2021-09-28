from collections import deque

def bfs(graph, i, j):
	q=deque()
	q.append((i,j))
	count = 0
	dx =[-1,1,0,0]
	dy = [0,0,-1,1]
	while(q):
		x, y = q.popleft()
		for k in range(len(dx)):
			if x+dx[k]<0 or y+dy[k]<0 or x+dx[k]>=len(graph) or y+dy[k]>=len(graph[0]):
				continue
			if graph[x+dx[k]][y+dy[k]] == 1:
				graph[x+dx[k]][y+dy[k]]= graph[x][y]+1
				q.append((x+dx[k], y+dy[k]))

	print(graph)
	print(graph[len(graph)-1][len(graph)-1])
				
graph=[]
n, m= map(int, input().split())
for i in range(n):
	temp = list(map(int, input()))
	graph.append(temp)

bfs(graph, 0,0)
