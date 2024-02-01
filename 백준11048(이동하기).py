n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
for i in range(n):
  for j in range(m):
    if i == 0 and j == 0: continue
    if i == 0:
      arr[i][j] += arr[i][j-1]
      continue
    if j==0:
      arr[i][j]+=arr[i-1][j]
      continue      
    arr[i][j]+=max(arr[i-1][j], arr[i-1][j-1], arr[i][j-1])
print(arr[n-1][m-1])
