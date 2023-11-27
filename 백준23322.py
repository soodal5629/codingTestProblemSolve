n, k = map(int, input().split())
arr = list(map(int, input().split()))
index = k
day = 0
cnt = 0
while index < n:
  arr.sort()
  if arr[index] > arr[index-k]:
    day+=1
    cnt += (arr[index]-arr[index-k])
    arr[index] = arr[index-k]
  else:
    index+=1
print(cnt, day)
