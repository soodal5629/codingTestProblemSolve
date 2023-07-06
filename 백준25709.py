n = input()
answer = 0
if len(n) < 1:
  answer = n
else:
  while n != '' :
    if int(n) == 0: break
    if n.count('1') != 0 and len(n)>1:
      answer += n.count('1')
      n = n.replace('1', '')
    else:
      n = str(int(n) - 1)
      answer+=1
  print(answer)
  
