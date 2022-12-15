import heapq
def solution(n, works):
    answer = 0
    arr = []
    for i in works:
        heapq.heappush(arr, -i)
    while n > 0:
        m = -heapq.heappop(arr)
        if m == 0: break
        heapq.heappush(arr, -(m-1))
        n-=1
    for i in arr:
        answer+= i**2
    return answer
