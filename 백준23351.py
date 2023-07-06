import heapq
n, k, a, b = list(map(int, input().split()))
arr = [k] * n
heapq.heapify(arr)
flag = True
day = 1
while flag:
  cnt = 0
  while cnt < a:
    temp = heapq.heappop(arr)
    temp += b
    heapq.heappush(arr, temp)
    cnt+=1
  for i in range(n):
    arr[i] -= 1
    if arr[i] == 0:
      flag = False
      break
  day+=1
print(day-1)
