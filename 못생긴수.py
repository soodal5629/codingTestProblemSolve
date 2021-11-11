n=int(input())
list = [False for _ in range(1500)]
list[1] = True
res = [-1 for _ in range(1500)]
list[2] = True
list[3] = True
list[5] = True
for i in range(2, 1500):
	if i==2 or i==3 or i==5: continue
	if i%2 ==0 and list[i//2]: list[i] = True
	elif i%3 ==0 and list[i//3]: list[i] = True
	elif i%5 ==0 and list[i//5]: list[i] = True
count = 0
for i in range(1500):
	if list[i]:
		res[count] = i
		count+=1
print(res[:n+1])
print(res[n-1])
