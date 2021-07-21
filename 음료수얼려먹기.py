def dfs(ice, visit, i,j):
	if ice[i][j] == 0 and visit[i][j] == False:
		visit[i][j] = True
		ice[i][j] = 2
		if i>0: dfs(ice, visit, i-1,j)
		if j<m-1: dfs(ice, visit, i,j+1)
		if j>0: dfs(ice, visit, i,j-1)
		if i<n-1: dfs(ice, visit, i+1,j)
		return True
	else: return False
ice = []
n,m =map(int,input().split())
for i in range(n):
  temp = list(map(int, input()))
  ice.append(temp)
visit = [[False for col in range(m)]for row in range(n)]
count = 0

for i in range(len(ice)):
	for j in range(len(ice[i])):
		if dfs(ice, visit, i,j):
			count+=1
print(ice)
print(count)
