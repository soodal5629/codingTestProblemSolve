from collections import deque

def find(s):
  d = deque()
  cnt = 0
  for i in s:
    if len(d) == 0:
      d.append(i)
      continue
    top = d[-1]
    if top == '{' and top != i:
      d.pop()
    else:
      d.append(i)
  for i in range(0, len(d)-1, 2):
    if d[i] == d[i+1]: cnt+=1
    else: cnt+=2

  return cnt
    
arr = []
while True:
  s = input()
  if '-' in s: break
  arr.append(s)
res = []
for i in range(len(arr)):
  res.append(find(arr[i]))

for i in range(len(res)):
  print("%d. %d" %(i+1, res[i])) 
