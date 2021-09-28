from collections import deque

def bfs(miro, visit, i, j,n,m):
	visit[i][j] = True
	q = deque()
	miro[i][j] = 2
	q.append((i,j))
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	while q:
		count = 0
		i, j = q.popleft()
		if i==n-1 and j==m-1:
			miro[i][j] = 2
			break
		if i>0 and miro[i-1][j] ==1:
			#miro[i-1][j] = 2
			q.append((i-1,j))
			count+=1
		if i<n-1 and miro[i+1][j] ==1:
			q.append((i+1,j))
			#miro[i+1][j] = 2
			count+=1
		if j>0 and miro[i][j-1] ==1:
			#miro[i][j-1] =2
			q.append((i,j-1))
			count+=1
		if j<m-1 and miro[i][j+1] ==1:
			#miro[i][j+1]=2
			q.append((i,j+1))
			count+=1
		if count == 0:
			miro[i][j] = 3
		else: miro[i][j] = 2

	
n,m = map(int, input().split())
miro = []
for i in range(n):
	temp = list(map(int, input()))
	miro.append(temp)
visit = [[False for _ in range(m)] for _ in range(n)]
bfs(miro, visit, 0,0,n,m)
print(miro)
count = 0
for i in range(n):
	for j in range(m):
		if miro[i][j] == 2:
			count+=1

print(count)
