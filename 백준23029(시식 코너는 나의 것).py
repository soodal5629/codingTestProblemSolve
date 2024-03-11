n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
d = [0] * n
d[0] = arr[0]
for i in range(1, n):
  if i == 1: d[i] = max(arr[i], arr[i]//2+d[i-1])
  elif i == 2:
    d[i] = max(arr[i]+d[i-2], arr[i]//2+arr[i-1], d[i-1])
  else:
    d[i] = max(arr[i]+d[i-2], (arr[i]//2)+arr[i-1]+d[i-3], d[i-1])
print(max(d))
