def distinguish(flag, temp, d, i):
  if not flag: return temp + d[i]
  else: return temp + d[i] +1
    
w = int(input())
d = dict()
d['WELCOME'] = 7
d['TO'] = 2
d['CCC'] = 3
d['GOOD'] = 4
d['LUCK'] = 4
d['TODAY'] = 5
arr = []
temp = 0
flag = False
temp2 = []
for i in d.keys():
  dis = distinguish(flag, temp, d, i)
  if dis <= w:
    if not flag:
      temp += d[i]
      flag = True
    else:
      temp += d[i] + 1
    temp2.append(i)
  else:
    arr.append(temp2)
    temp2 = []
    temp2.append(i)
    temp = d[i]
if len(temp2) > 0: arr.append(temp2)
for i in arr:
  s = w - len(''.join(i))
  if len(i)>1:
    while s > 0 :
      for j in range(len(i)-1):
        if s > 0:
          i[j]+='.'
          s-=1
  else: i[0]+= '.'*s

for s in arr:
  print(''.join(s))
