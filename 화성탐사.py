import heapq

INF = int(1e9)

def find_min(graph, distance):
	q= []
	n=len(graph)
	heapq.heappush(q, (graph[0][0], (0,0)))
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	distance[0][0] = graph[0][0]
	while(q):
		dist, index = heapq.heappop(q)	
		for i in range(len(dx)):
			if index[0]+dx[i]<0 or index[1]+dy[i]<0 or index[0]+dx[i]>=n or index[1]+dy[i]>=n:
				continue
			cost = dist + graph[index[0]+dx[i]][index[1]+dy[i]]
			if cost<distance[index[0]+dx[i]][index[1]+dy[i]]:
				#print("i=",index[0]+dx[i], "j=", index[1]+dy[i], "cost=", cost)
				distance[index[0]+dx[i]][index[1]+dy[i]] = cost
				heapq.heappush(q, (cost, (index[0]+dx[i], index[1]+dy[i])))
	print(distance[n-1][n-1])
	# for i in range(n):
	# 	for j in range(n):
	# 		print(distance[i][j], end=" ")
	# 	print()
	
		

t= int(input())

for i in range(t):
	n = int(input())
	graph=[]
	for i in range(n):
		graph.append(list(map(int, input().split())))
	distance = [[INF for _ in range(n)]for row in range(n)]
	find_min(graph, distance)


