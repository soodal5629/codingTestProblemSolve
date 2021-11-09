def solution(money, m):
	arr = [1e9]*(10001)
	for i in money:
		arr[i] = 1
	for i in range(1,m+1):
		for j in money:
			arr[i] = min(arr[i-j]+arr[j], arr[i])
	if arr[m]==1e9: print(-1)
	else: print(arr[m])

n,m=map(int, input().split())
money=[]
for i in range(n):
	money.append(int(input()))
solution(money, m)
