from collections import deque
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
s = 0
d = deque([0] * k)
temp = 0
cnt = 0
for i in range(n):
  cnt+=1
  temp += (d[i%k] + arr[i])
  d[i%k] += arr[i]
  if cnt == k or i == n-1:
    cnt = 0
    s+=temp
    temp = 0
print(s)
