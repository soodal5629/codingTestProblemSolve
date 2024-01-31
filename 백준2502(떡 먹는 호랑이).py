d, k = map(int, input().split())
arr = ['x', 'y']
for i in range(2, d):
  arr.append(arr[i-1]+arr[i-2])
x = arr[d-1].count('x')
y = arr[d-1].count('y')
fir = sec = 0
for i in range(1, k):
  for j in range(1, k):
    if (i*x) + (j*y) == k and i <= j:
      fir = i
      sec= j
      break
  if fir != 0  and sec != 0: break
print(fir)
print(sec)
