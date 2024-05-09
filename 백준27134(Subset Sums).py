from collections import defaultdict
n = int(input())
arr = [i for i in range(1, n+1)]
if sum(arr)%2 != 0:
  print(0)
else:
  temp = [1]
  v = sum(arr)//2
  d = defaultdict(int)
  d[1] = 1
  for now in range(2, n+1):
    temp2 = defaultdict(int)
    for j in d.keys():
      if d[j] == 0: continue
      if j+now <= v:
        temp2[j]+=d[j]
    for j in temp2:
      d[now+j]+=temp2[j]
    d[now]+=1
  print(d[v]//2)
