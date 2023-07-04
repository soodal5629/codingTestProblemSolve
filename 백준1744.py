import heapq
n = int(input())
q1 = []
q2 = []
for i in range(n):
  test = int(input())
  if test <= 0:
    heapq.heappush(q1, test)
  else:
    heapq.heappush(q2, -test)
answer = 0

while q1:
  test = heapq.heappop(q1)
  if q1:
    test2 = heapq.heappop(q1)
    answer += max(test*test2,test+test2)
  else:
    answer += test
while q2:
  test = -heapq.heappop(q2)
  if q2:
    test2 = -heapq.heappop(q2)
    answer += max(test*test2, test+test2)
  else:
    answer += test
print(answer)
