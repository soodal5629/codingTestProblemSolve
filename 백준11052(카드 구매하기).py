n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
d = [0] * (n+1)
d[1] = arr[1]
res = -1
for i in range(1, n+1):
  for j in range(i):
    if j != 0 and i % j == 0:
      d[i] = max(d[i], arr[j]*(i//j))
    d[i] = max(d[i], arr[i], arr[i-j] + d[j])
print(d[n])
