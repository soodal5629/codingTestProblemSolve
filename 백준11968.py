n = int(input())
b = [i for i in range(1, (2*n)+1)]
e = []
for i in range(n):
  temp = int(input())
  e.append(temp)
  b.remove(temp)
e.sort()
b.sort()
res = 0
index = 0
for i in range(n):
  if e[i] < b[index]:
    res+=1
    index+=1
  else:
    while index < n:
      if e[i] < b[index]:
        res+=1
        index+=1
        break
      index+=1
  if index >= n: break
print(res)
