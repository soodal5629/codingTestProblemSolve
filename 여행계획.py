def find_root(parent, x):
	while x!=parent[x]:
		x= parent[parent[x]]
	return x

def union(a, b, parent):
	a = find_root(parent, a)
	b = find_root(parent, b)
	if a<b: parent[b] = a
	else: parent[a] = b
	return parent

n,m= map(int, input().split())
graph = []
for i in range(n):
	graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))
parent = [0 for i in range(n+1)]
for i in range(n+1):
	parent[i] = i
edge = [[] for i in range(n+1)]
for i in range(n):
	for j in range(n):
		if graph[i][j] == 0: continue
		else: edge[i+1].append(j+1)

for i in range(1, n+1):
	for j in range(len(edge[i])):
		if find_root(parent, i) != find_root(parent, edge[i][j]):
			union(i, edge[i][j], parent)
flag = True
for i in range(len(plan)-1):
	for j in range(i+1, len(plan)):
		if find_root(parent, plan[i])!=find_root(parent, plan[j]):
			flag = False
if flag: print("yes")
else: print("no")

			
		
