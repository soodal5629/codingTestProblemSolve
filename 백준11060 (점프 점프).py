n = int(input())
arr = list(map(int, input().split()))
d = [1e9] * n
d[0] = 0
cnt = 0
for i in range(n-1):
  for j in range(i+1, i+arr[i]+1):
    if j < n:
      d[j] = min(d[j], d[i] + 1)
res = -1
if d[n-1] == 1e9: -1
else: res = d[n-1]
print(res)
