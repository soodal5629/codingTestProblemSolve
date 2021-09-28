from collections import deque

def dfs(graph, i, j):
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	if graph[i][j] == 0:
		graph[i][j] = 2
		for k in range(4):
			if i+dx[k]<0 or i+dx[k]>=len(graph) or j+dy[k]<0 or j+dy[k]>=len(graph[0]):
				continue
			else:
				dfs(graph, i+dx[k], j+dy[k])
		return True
	return False

graph=[]
n, m= map(int, input().split())
for i in range(n):
	temp = list(map(int, input()))
	graph.append(temp)

count = 0
for i in range(n):
	for j in range(m):
		if dfs(graph,i,j):
			count+=1
print(count)
