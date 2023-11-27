n = int(input())
arr = list(map(int, input().split()))
arr.sort()
l = 0
r = n-1
res = 0
while l <= r:
  if r-l <= 1:
    res += arr[r]
    break
  else:
    res+=(arr[r] - arr[l])
    l+=1
    r-=1
print(res)
