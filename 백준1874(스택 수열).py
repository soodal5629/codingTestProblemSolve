from collections import deque, defaultdict
dict = defaultdict(int)
n = int(input())
arr = []
for i in range(n):
  arr.append(int(input()))
num = deque([i for i in range(1, n+1)])
d = deque()
res = []
index = index2 = 0
temp = []
while index < n:
  b = len(d)
  if d and d[-1] == arr[index]:
    temp.append(d.pop())
    res.append('-')
    index+=1
  else:
    res.append('+')
    if dict[num[index2]] == 0:
        dict[num[index2]] = 1
        d.append(num[index2])
    if index2 < len(num)-1: index2+=1
  if b == len(d): break
if len(arr)!=len(temp):
  print('NO')
else:
  flag = True
  for i in range(n):
    if arr[i] != temp[i]:
      flag = False
      break
  if flag:
    for i in range(len(res)):
      print(res[i])
  else:
    print('NO')
