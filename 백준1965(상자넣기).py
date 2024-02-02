n = int(input())
arr = list(map(int, input().split()))
d = [1] * n
for i in range(1, n):
  for j in range(i-1, -1, -1):
    if arr[j] < arr[i]:
      d[i] = max(d[j]+1, d[i])
    elif arr[j] == arr[i]:
      d[i] = max(d[i], d[j])
print(max(d))
