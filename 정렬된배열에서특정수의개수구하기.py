import sys

count = 0
def binary(arr, n, x, start, end, visit):
	global count

	while start<=end:
		mid = (start+end)//2
		if mid >= n : break
		if arr[mid] == x and visit[mid] == False:
			count +=1
			visit[mid] = True
			binary(arr, n, x, mid+1, end, visit)
			binary(arr, n, x, start, mid-1, visit)
		elif arr[mid]<x:
			start = mid+1
		else:
			end=mid-1
	return count


n, x= map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
visit = [False] * n
res = binary(arr, n, x, 0, n, visit)
if res>0:
	print(res)
else:
	print(-1)
