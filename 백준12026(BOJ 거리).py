n = int(input())
s = input()
d = [1e9] * n
d[0] = 0
for i in range(1, n):
  now = s[i]
  if now == 'B':
    for j in range(i-1, -1, -1):
      if s[j] == 'J':
        d[i] = min(d[i], d[j]+(i-j)**2)
  elif now == 'O':
    for j in range(i-1, -1, -1):
      if s[j] == 'B':
        d[i] = min(d[i], d[j]+(i-j)**2)
  else: # J
    for j in range(i-1, -1, -1):
      if s[j] == 'O':
        d[i] = min(d[i], d[j]+(i-j)**2)
if d[n-1] == 1e9: print(-1)
else: print(d[n-1])
