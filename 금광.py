def gold(area):
	for i in range(1, len(area[0])):
		for j in range(len(area)):
			if j==0: area[j][i] = max(area[j][i-1], area[j+1][i-1])+area[j][i]
			elif j==len(area)-1: area[j][i] = max(area[j][i-1], area[j-1][i-1])+area[j][i]
			else: area[j][i] = max(area[j][i-1], area[j+1][i-1], area[j-1][i-1])+area[j][i]
	raw = len(area[0])
	res = 0
	for i in range(len(area)):
		res = max(area[i][len(area[0])-1], res)
	print(res)
	print(area)

t=int(input())
for i in range(t):
	n, m = map(int, input().split())
	area = [[-1 for cols in range(m)] for rows in range(n)]
	temp = list(map(int, input().split()))
	index=0
	for j in range(n):
		for k in range(m):
			area[j][k] = temp[index]
			index += 1
	gold(area)
