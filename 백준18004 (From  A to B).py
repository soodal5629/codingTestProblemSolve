a, b= list(map(int, input().split()))
cnt = 0
if a < b:
  cnt = (b-a)
elif a == b:
  cnt = 0
else:
  while a != b:
    if a > b and a%2==0:
      a = a//2
      cnt+=1
    else:
      cnt += 1
      a +=1
print(cnt)
