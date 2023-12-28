def modify_zero(s):
  return s[0] + '0' +s[1:]
  
while True:
  arr = list(map(int, input().split()))
  if arr[0] == 0: break
  arr = arr[1:]
  f = s = ''
  arr.sort(reverse = True)

  for i in range(len(arr)):     
    if arr[i] == 0: break
    if i %2 == 0:
      s += str(arr[i])
    else:
      f+=str(arr[i])
  f = f[::-1]
  s = s[::-1]

  for i in range(arr.count(0)):
    if len(f)<len(s):
      f = modify_zero(f)
    elif len(s)>len(f):
      s = modify_zero(s)
    else:
      if int(f) < int(s):
        f = modify_zero(f)
      else:
        s = modify_zero(s)
  print(int(f) + int(s))
