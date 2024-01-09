d = dict()
d['.--'] = 'A'
d['-.'] = 'B'
d['---'] = 'C'
d['..'] = 'D'
d['--..'] = 'E'
d['--.-'] = 'F'
d['.-.'] = 'G'

while True:
  try:
    s = input()
    if s == '': break
    index = 0
    temp = ''
    while len(s)>1 and index < len(s):
      if s[:index+1] in d.keys():
        temp += d[s[:index+1]]
        s = s[index+1:]
        index = 0
      else:
        index+=1
    if len(s) >= 1:
      temp = 'could not be translated'
    print(temp)  
  except EOFError: break
