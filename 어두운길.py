def find_root(x, parent):
	while x!=parent[x]:
		x = parent[parent[x]]
	return x
def union(a, b, parent):
	a = find_root(a, parent)
	b = find_root(b, parent)
	if a<b: parent[b] = a
	else: parentp[a] =b
	return parent
		
n, m = map(int, input().split())
graph = []
for i in range(m):
	a,b,c = map(int, input().split())
	graph.append((c, a, b))
parent = [0 for _ in range(n)]
for i in range(n):
	parent[i] = i
graph.sort()
total = 0
sum = 0
for i in range(m):
	cost, a, b = graph[i]
	total += cost
	if find_root(a, parent) != find_root(b, parent):
		union(a, b, parent)
		sum += cost
print(total-sum)
