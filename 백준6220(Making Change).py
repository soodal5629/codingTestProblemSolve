c, n = map(int, input().split())
arr = []
d = [1e9] * (c+1)
d[0] = 0
for i in range(n):
  temp = int(input())
  arr.append(temp)
  if temp <= c+1: d[temp] = 1

for i in range(1, c+1):
  for coin in arr:
    if i > coin and i%coin == 0:
      d[i] = min(d[i], i//coin)
    if i >= coin:
      d[i] = min(d[i], d[i-coin] + d[coin])
print(d[c])
