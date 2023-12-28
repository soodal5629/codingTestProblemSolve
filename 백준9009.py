def find(f, n):
  for i in range(len(f)-1, -1, -1):
    if f[i] <= n:
      return f[i]

t = int(input())
f = [0, 1]
n = 1000000000
i = 2
while True:
  f.append(f[i-1] + f[i-2])
  if f[i] > 1000000000: break
  i +=1

for k in range(t):
  n = int(input())
  arr = []
  while n > 0:
    temp = find(f, n)
    n -= temp
    arr.append(temp)
  arr.sort()
  for i in arr:
    print(i, end = ' ')    
