from collections import deque

def infection(graph, x, y, k, t):
	q= deque()
	for c in range(1, k+1):
		for i in range(len(graph)):
			for j in range(len(graph)):
				if graph[i][j] == c:
					q.append((c, i, j, 0))
	count=1
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	while q:
		value, i, j, time = q.popleft()
		if time < t:
			for index in range(4):
				if i+dx[index]>=0 and i+dx[index]<len(graph) and j+dy[index]>=0 and j+dy[index]<len(graph):
					if graph[i+dx[index]][j+dy[index]] == 0:
						graph[i+dx[index]][j+dy[index]] = value
						q.append((value, i+dx[index], j+dy[index], time+1))
		else: break
	print(graph[x-1][y-1])
	
n,k=map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
t, x, y=map(int, input().split())
infection(graph, x, y, k, t)
