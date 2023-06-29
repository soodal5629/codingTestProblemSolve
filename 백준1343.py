s = input()
index = []
for i in range(len(s)):
  if s[i] == '.': index.append(i)
arr = s.split('.')
answer = ''

for i in arr:
  if i == '.':
    answer += '.'
  elif len(i) % 2 == 1:
    answer = -1
    break
  elif len(i) % 4 == 0:
    answer += 'A'*len(i)
  elif len(i) == 2:
    answer += 'B'*2
  else:
    a = len(i)//4 *'AAAA'
    b = (len(i) % 4) * 'B'
    answer += (a+b)
if answer != -1:
  for i in index:
    answer = answer[:i] + '.' + answer[i:]
print(answer)
