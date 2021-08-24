n, m= map(int, input().split())
data = []
for i in range(n):
	temp = list(map(int, input().split()))
	data.append(min(temp))
print(max(data))
