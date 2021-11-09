def make_one(n):
	num = [0]* (n+1)
	num[1] = 1
	num[2] = 1
	num[3] =1 
	num[5] = 1
	for i in range(2,n+1):
		if i==2 or i==3 or i==5: continue
		if i%5==0: num[i] = min(1+num[i//5], 1+num[i-1])
		elif i%3==0: num[i] = min(1+num[i//3], 1+num[i-1])
		elif i%2==0: num[i] = min(1+num[i//2], 1+num[i-1])
		else: num[i] = 1+num[i-1]
	#print(num)
	print(num[n])

n = int(input())
make_one(n)
