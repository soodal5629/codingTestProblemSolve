s = input()
h, m = map(int, s.split(':'))
cnt = 0
flag = False
if m >= 30:
  a, b = divmod(m, 30)
  cnt += a
  cnt += (b//10)
  m = 0
  flag = True
if h > 9:
  cnt += (h//10)
  h = h%10
  if flag == False:
    flag = True
    cnt+=1
if h > 0:
  cnt += h
  if flag == False:
    flag = True
    cnt+=1
if 0 < m < 30:
  cnt += (m//10)
  if flag == False: cnt+=1

print(cnt)
  
