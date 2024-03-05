import copy
n = int(input())
arr = list(map(int, input().split()))
d = copy.deepcopy(arr)
for i in range(1, n):
  for j in range(i):
    if arr[j] < arr[i]:
      d[i] = max(d[j]+arr[i], d[i])
print(max(d))
