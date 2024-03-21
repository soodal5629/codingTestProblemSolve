from collections import defaultdict
n = int(input())
temp = 1
cnt = 1
dict = defaultdict(int)
while True:
  before = temp
  temp+=cnt    
  if temp!=cnt: cnt = before
  if temp == 2: dict[temp] = 1
  else: dict[temp] = cnt
  if cnt > n: break
s = [1e9] * (n+1)
m = [0] * (n+1)
for i in range(2, n+1):
  for k in dict.copy().keys():
    if i % k == 0:
      s[i] = min(s[i], dict[k] * (i//k))
      m[i] = max(m[i], dict[k] * (i//k))
    if i>=k and i-k in dict.keys() and dict[i-k] != 0:
      s[i] = min(s[i], s[i-k]+dict[k])
      m[i] = max(m[i], m[i-k]+dict[k])
  for j in range(2, i):
    if i % j== 0:
      s[i] = min(s[i], s[j]*(i//j))
      m[i] = max(m[i], m[j]*(i//j))
    s[i] = min(s[i], s[i-j] + s[j])
    m[i] = max(m[i], m[i-j]+m[j])
print(s[n], m[n])
