from collections import defaultdict
n = int(input())
arr = []
for i in range(n):
  arr.append(input())

arr.sort(key = lambda x:-len(x))
print(arr)
d = defaultdict(int)
for i in arr:
  flag = False
  for j in d.keys():
    if j.startswith(i):
      flag = True
      break
  if flag == False:
    d[i] = 1

print(len(d.keys()))
    
