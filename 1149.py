n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

for i in range(1, n):
  for j in range(3):
    if j == 0: arr[i][j] += min(arr[i-1][1], arr[i-1][2])
    elif j == 1: arr[i][j] += min(arr[i-1][0], arr[i-1][2])
    else: arr[i][j] += min(arr[i-1][0], arr[i-1][1])

print(min(arr[n-1]))
