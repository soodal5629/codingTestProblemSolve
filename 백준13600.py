n = int(input())
arr = [0] * 10
arr[1] = 1
for i in range(2, 10):
  arr[i] = arr[i-1] * i

cnt = 0
while n > 0:
  for i in range(10):
    if n < arr[i]:
      n -= arr[i-1]
      cnt+=1
      break
print(cnt)
