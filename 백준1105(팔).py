l, r = map(int, input().split())
res = 1e9
if l == r:
  res = str(r).count('8')
elif str(r).count('8') == 0 or str(l).count('8') == 0: res = 0
elif len(str(l)) == len(str(r)):
  cnt = 0
  for i in range(len(str(l))):
    if str(l)[i] == str(r)[i] and str(l)[i] == '8':
      cnt+=1
    elif str(l)[i] == str(r)[i]: continue
    else:
      break
  res = cnt
else: res = 0
print(res)
