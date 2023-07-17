n = int(input())
for i in range(n):
  s, k = input().split()
  k = int(k)
  arr = list(s)
  index = 0
  cnt = 0
  while index < len(s):
    if arr[index] == '-':
      temp = 1
      if index + k > len(s):
        cnt = -1
        break
      arr[index] = '+'
      while temp < k:
        if arr[index+temp] == '-':
          arr[index+temp] = '+'
        else:
          arr[index+temp] = '-'
        temp +=1
      cnt+=1
    index+=1
  s = ''
  if cnt != -1: s = "Case #"+str(i+1)+ ": " + str(cnt)
  else: s = "Case #" +  str(i+1)+ ": IMPOSSIBLE"
  print(s)
  
