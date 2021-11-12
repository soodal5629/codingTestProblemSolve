def max_pro(n, t, p):
	arr = [0] * (n+2)
	for i in range(n, 0, -1):
		if i+t[i]>(n+1): 
			arr[i] = arr[i+1]
			continue
		arr[i] = max(arr[i+1], p[i]+arr[i+t[i]])
	print(max(arr))

n=int(input())
t = [0]*(n+1)
p = [0]*(n+1)
for i in range(1,n+1):
	t[i], p[i] = map(int, input().split())

max_pro(n, t, p)
