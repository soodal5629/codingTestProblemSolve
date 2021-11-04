import sys

def binary(arr, start, end, res):
	while start<=end:
		mid = (start+end)//2
		if mid >= len(arr): break
		if mid == arr[mid] and res.count(mid)==0:
			print(mid)
			res.append(mid)
			binary(arr, start, mid-1, res)
			binary(arr, mid+1, end, res)
		elif mid<arr[mid]:
			end = mid-1
		else:
			start = mid+1
	return res
		
				

n = int(input())
arr = list(map(int, input().split()))
res = []
res = binary(arr, 0, n, res)
if res:
	for i in res:
		print(i, end=" ")
else: print(-1)
