import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    q = scoville
    now = 0
    while q:
        mini = heapq.heappop(q)
        if mini>=K:
            break
        if q: next_mini = heapq.heappop(q)
        else: break
        now = mini + 2*next_mini
        answer +=1
        heapq.heappush(q, now)
    if now<K:
        answer = -1
    return answer
