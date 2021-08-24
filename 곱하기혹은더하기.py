s= input()
data = list(s)

res = 0
for i in data:
	i = int(i)
	if i == 0 or res ==0:
		res +=i
	else:
		res *= i
print(res)
