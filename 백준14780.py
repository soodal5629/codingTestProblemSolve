import heapq

n = int(input())
q = []
for i in range(n):
  a, b = map(int, input().split())
  heapq.heappush(q, [a+b, a, b] )
cnt = 0 
now = 0
while q:
  s, start, end = heapq.heappop(q)
  if now <= start:
    now = s
    cnt +=1
print(cnt)
