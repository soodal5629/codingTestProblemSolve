t = int(input())
for k in range(t):
  n = int(input())
  arr = list(map(int, input().split()))
  temp = []
  cnt = 0
  c = 1
  while c <= n:
    index = arr.index(c)
    if index > c - 1:
      while index != c-1:
        arr[index-1], arr[index] = arr[index], arr[index-1]
        index -= 1
        cnt+=1
    else:
      while index!= c-1:
        arr[index+1], arr[index] = arr[index], arr[index+1]
        index += 1
        cnt+=1
    c+=1
  print(cnt)
  
