def excused(n, soldier):
	list = [1 for i in range(n)]
	for i in range(n-1,-1,-1):
		if i==n-1:
			continue
		for j in range(n-1, i, -1):
			if soldier[i]>soldier[j]:
				list[i]=max(list[j]+1, list[i])			
	print(n-max(list))

n = int(input())
soldier = list(map(int, input().split()))
excused(n, soldier)
