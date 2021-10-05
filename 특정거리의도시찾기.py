from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, k, x, visit):
	q = deque()
	visit[x] = True
	distance = [0 for _ in range(len(graph))]
	q.append(x)	
	while(q):
		now = q.popleft()
		for i in graph[now]:
			if visit[i] == True:
				continue
			else:
				visit[i] = True
				distance[i] = distance[now]+1
				q.append(i)
	if distance.count(k) ==0:
		print(-1)
	else:
		for i in range(1, len(distance)):
			if distance[i] == k:
				print(i)
			

n,m,k,x =map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
	a,b = map(int, input().split())
	graph[a].append(b)

visit = [False for _ in range(n+1)]
bfs(graph, k, x, visit)
