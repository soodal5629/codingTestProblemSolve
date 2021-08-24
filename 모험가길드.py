n = int(input())
data = list(map(int, input().split()))
count = 0
res = 0
data.sort()
for i in data:
	count +=1
	if count>=i:
		res+=1
		count = 0

print(res)
