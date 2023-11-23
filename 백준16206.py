n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
arr.sort(key = lambda x: (x%10, x))
for i in arr:
  if i < 10: continue
  elif i == 0: cnt+=1
  elif i % 10 == 0:
    if m >= ((i // 10)-1):
      cnt += i//10
      m -= ((i // 10)-1)
    else:
      cnt += m
      break
  else:
    if m >=(i//10):
      cnt += (i//10)
      m -= (i//10)
    else:
      cnt += m
      break
print(cnt)
