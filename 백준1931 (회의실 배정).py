n = int(input())
arr = []
for i in range(n):
  s, e = map(int, input().split())
  arr.append([s, e])
arr.sort(key = lambda x:(x[1], x[0]))
res = 1
s = arr[0][0]
e = arr[0][1]
for i in range(1, n):
  if arr[i][0] >= e:
    s = arr[i][0]
    e = arr[i][1]
    res+=1
print(res)
