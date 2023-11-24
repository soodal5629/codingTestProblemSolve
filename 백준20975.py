n = int(input())
cow = list(map(int, input().split()))
h = list(map(int, input().split()))
cow.sort(reverse = True)
h.sort(reverse = True)
res = 1
arr = []

for i in range(len(cow)):
  temp = 0
  for j in h:
    if j >= cow[i]:
      temp+=1
    else:
      break
  if i == 0:
    arr.append(temp)
  else:
    arr.append(temp-i)
for i in arr:
  res *= i
print(res)
