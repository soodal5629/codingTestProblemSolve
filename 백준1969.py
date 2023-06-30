from collections import defaultdict
n, m = list(map(int, input().split()))
arr = []
for i in range(n):
  arr.append(input())
arr2 = [0] * m
for i in range(m):
  temp = defaultdict(int)
  for j in range(n):
    temp[arr[j][i]] +=1
  max_key = max(temp, key = lambda k:(temp[k], -ord(k)))

  arr2[i] = max_key
s = ''.join(arr2)
print(s)
cnt = 0
for i in range(n):
  temp = arr[i]
  for j in range(m):
    if s[j] != temp[j]: cnt+=1
print(cnt)
