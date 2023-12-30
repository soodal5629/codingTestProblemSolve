def convert(num):
  if num == 0: return 1
  else: return 0
  
n = int(input())
arr = list(map(int, input().split()))
temp = [0] * n
cnt = 0
for i in range(n):
  if arr[i] != temp[i]:
    cnt+=1
    temp[i] = arr[i]
    if i+1 < n:
      temp[i+1] = convert(temp[i+1])
    if i+2 < n: temp[i+2] = convert(temp[i+2])
print(temp, cnt)
