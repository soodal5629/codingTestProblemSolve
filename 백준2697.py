n = int(input())
for index in range(n):
  num = int(input())
  s = list(map(int, str(num)))
  arr = []
  temp = []
  for i in s: temp.append(i)
  for j in range(len(s)-1, -1, -1):
    now = s[j]
    for k in range(j-1, -1, -1):
      if now > s[k]:
        s[j], s[k] = s[k], s[j]
        a = ''.join(map(str, s[k+1:]))
        b = list(map(str, s[:k+1]))
        temp2 = b + sorted(a)
        if num < int(''.join(temp2)): arr.append(int(''.join(temp2)))
        break
    s= []
    for i in temp: s.append(i)
  if len(arr) == 0: print("BIGGEST")
  else: print(min(arr))
