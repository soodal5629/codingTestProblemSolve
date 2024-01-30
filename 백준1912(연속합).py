n = int(input())
arr = list(map(int, input().split()))
d = [i for i in arr]
for i in range(1, n):
  if d[i-1] + d[i] > d[i]:
    d[i] = d[i-1]+d[i]
print(max(d))
