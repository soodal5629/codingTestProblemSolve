n, l = input().split()
arr = list(map(int, input().split()))
arr.sort()
res = 1
x = arr[0] - 0.5 + int(l)

for i in range(1, int(n)):
  if x > arr[i]:
    continue
  else:
    res+=1
    x = arr[i] - 0.5 + int(l)

print(res)
