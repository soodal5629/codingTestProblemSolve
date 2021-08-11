from collections import deque

def topology(indegree, edge, time):
	q= deque()
	for i in range(1, len(indegree)):
		if indegree[i] == 0:
			q.append(i)
	while(q):
		now = q.popleft()
		cost = time[now]
		for i in edge[now]:
			indegree[i] -=1
			if indegree[i] == 0:
				q.append(i)
				time[i] += cost
	print(time[1:])

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(1, n+1):
	data = list(map(int, input().split()))
	for j in data:
		graph[i].append(j)		

indegree = [0 for i in range(n+1)]
time = [0 for i in range(n+1)]
edge = [[] for _ in range(n+1)]
for i in range(1, len(graph)):
	for j in range(0, len(graph[i])):
		if j==0:
			time[i] = graph[i][0]
			continue
		elif graph[i][j]== -1: 

			continue
		else:
			indegree[i] += 1
			edge[graph[i][j]].append(i)
topology(indegree, edge, time)
		
		
		
	
