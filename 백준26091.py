n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
l = 0
r = n-1
cnt = 0
while l < r:
  if arr[l] + arr[r] >= m:
    l +=1
    r-=1
    cnt+=1
  else:
    l+=1
print(cnt)
