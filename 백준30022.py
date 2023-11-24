n, a, b = map(int, input().split())
arr = []
for i in range(n):
  fir, sec = map(int, input().split())
  arr.append([abs(fir-sec),fir, sec])
arr.sort(key = lambda x:-x[0])

res = 0
for i in range(n):
  fir = arr[i][1]
  sec = arr[i][2]
  if a > 0 and  fir < sec:
    a -= 1
    res += fir
  elif b > 0 and fir > sec:
    b -= 1
    res += sec
  elif a == 0:
    res+= sec
    b -=1
  else:
    res+= fir
    a-=1
print(res)
