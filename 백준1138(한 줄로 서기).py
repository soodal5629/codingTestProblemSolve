n = int(input())
arr = list(map(int, input().split()))
temp = [0] * (n+1)
for i in range(len(arr)):
  index = arr[i]+1
  while index < n+1:
    if temp[index] == 0:
      cnt = 0
      for j in range(1, index):
        if temp[j] > i+1 or temp[j] == 0:
          cnt+=1
      if cnt == arr[i]:
        temp[index] = i+1
        break
    index+=1
for i in range(1, n+1):
  print(temp[i], end = ' ')
