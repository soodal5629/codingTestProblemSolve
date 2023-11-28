n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
index = set()
# 가로 방향
for i in range(n):
  temp = 0
  x = y = 0
  for j in range(m):
    if temp < arr[i][j]:
      temp = arr[i][j]
      x = i
      y = j
  index.add((x, y))

# 세로 방향
for i in range(m):
  temp = 0
  x = y = 0
  for j in range(n):
    if temp < arr[j][i]:
      temp = arr[j][i]
      x = j
      y = i
  index.add((x, y))

res = 0
for i in index:
  x, y = i
  res += arr[x][y]

s = 0
for i in range(n):
  s+=sum(arr[i])
print(s-res)
