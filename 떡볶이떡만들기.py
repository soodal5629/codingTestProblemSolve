import sys

def cut(list, m):
	list.sort()
	start = list[0]
	end = list[len(list)-1]
	res = 0
	while start<=end:
		mid = (start+end)//2
		temp = 0
		for i in list:
			if i>mid:
				temp += (i-mid)
		if temp<m:
			end = mid-1
		elif temp>=m:
			start = mid+1
			res = max(res, mid)
	print(res)
				
	
n, m = map(int, input().split())
dduck = list(map(int, sys.stdin.readline().split()))
cut(dduck, m)

