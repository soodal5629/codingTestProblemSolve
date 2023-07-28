s = input()
t = input()
res = 0

while len(t) >= len(s):
  if t[-1] == 'A':
    t = t[:-1]
  else:
    t = t[:-1]
    t = t[::-1]
  if s == t:
    res = 1

print(res)
