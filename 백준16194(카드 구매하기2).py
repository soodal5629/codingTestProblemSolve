n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
d = [0] * (n+1) 
d[1] = arr[1]
for i in range(1, n+1):
  for j in range(1, i):
    if j < i and i % j == 0:
      d[i] = min(arr[i], d[j]*(i//j))
    d[i] = min(d[i], arr[i], d[j]+d[i-j])
print(d[n])
