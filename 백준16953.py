a,b = list(map(int, input().split()))
cnt = 0
if a != b:
  while b > 0:
    cnt+=1
    if b % 2 ==1:
      if str(b)[-1] == '1':
        temp = str(b)[:-1]
        if temp != '': b = int(temp)
        else: break
      else: break
    elif b % 2 == 0:
      b = b // 2
    if b == a:
      break

if a == b: print(cnt+1)
else: print(-1)
