n = int(input())
arr = list(map(int, input().split()))
d = [1 for _ in range(n)]
for i in range(n-1):
  for j in range(i+1, n):
    if arr[i] > arr[j]:
      d[j] = max(d[i]+1, d[j])
res = max(d)
print(res)
