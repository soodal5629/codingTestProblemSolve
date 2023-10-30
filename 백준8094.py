w = int(input())
n = int(input())
d = []
for i in range(n):
  d.append(int(input()))
d.sort()
cnt = 0
left = 0
right = n-1
while left < right:
  if d[left]+d[right] <= w:
    cnt+=1
    d[left] = d[right] = 0
    left +=1
    right -=1
  else:
    right -=1
print(cnt + n - d.count(0))
