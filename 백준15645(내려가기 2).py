def find(arr, n, s):
  d = [[0 for _ in range(3)] for _ in range(n)]
  for i in range(n):
    for j in range(3):
      d[i][j] = arr[i][j]
  for i in range(1, n):
    for j in range(3):
      if j == 0:
        if s=='p':
          d[i][j] += max(d[i-1][j], d[i-1][j+1])
        else:
          d[i][j] += min(d[i-1][j], d[i-1][j+1])
      elif j == 1:
        if s=='p':
          d[i][j] += max(d[i-1][j], d[i-1][j+1], d[i-1][j-1])
        else:
          d[i][j] += min(d[i-1][j], d[i-1][j+1], d[i-1][j-1])
      else:
        if s=='p':
          d[i][j] += max(d[i-1][j], d[i-1][j-1])
        else:
          d[i][j] += min(d[i-1][j], d[i-1][j-1])
  if s == 'p':
    return max(d[n-1])
  else:
    return min(d[n-1])
    
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
a = find(arr, n, 'p') # plus - 최대
b = find(arr, n, 'm') # minus - 최소
print(a, b)
