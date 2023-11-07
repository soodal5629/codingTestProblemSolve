t = int(input())
for _ in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  arr.sort()
  temp = [0] * len(arr)
  l = 0
  r = len(arr) -1
  for i in range(len(arr)):
    if i%2 == 0:
      temp[l] = arr[i]
      l += 1
    else:
      temp[r] = arr[i]
      r -=1
  m = -1
  for i in range(len(arr)-1):
    m = max(m, abs(temp[i+1]-temp[i]))
  print(m)
