from collections import deque
t = int(input())
for k in range(t):
  num = list(input())
  
  for i in range(len(num)):
    if num[i] == '6':
      num[i] = '9'
  num.sort(reverse=True)
  num = deque(num)  
  first = num.popleft()
  sec = num.popleft()
  a = first
  b = sec
  while num:
    if int(a) >= int(b):
      if num:
        b += num.popleft()
        if num: a += num.popleft()
    else:
      if num:
        a += num.popleft()
        if num : b+=num.popleft()
        
  print(int(a)*int(b))
