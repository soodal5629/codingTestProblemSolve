def star_max(star):
	n = len(star)
	for i in range(1, n):
		for j in range(len(star[i])):
			if j==0: star[i][j] = star[i-1][j]+star[i][j]
			elif j==len(star[i])-1: star[i][j] = star[i-1][j-1]+star[i][j] # 조건문이 i==j여도 성립(더 간단)
			else: star[i][j] = max(star[i-1][j-1], star[i-1][j])+star[i][j]
	res = 0
	for i in range(n):
		res = max(star[n-1][i], res)
	print(res)

n=int(input())
star = []
for i in range(n):
	temp = list(map(int, input().split()))
	star.append(temp)
star_max(star)
