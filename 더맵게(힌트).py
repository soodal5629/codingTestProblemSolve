import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    first = heapq.heappop(scoville)
    while first<K and len(scoville)>=1:
        mix = first + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, mix)
        answer+=1
        first = heapq.heappop(scoville);
    
    if first<K: answer = -1
    return answer
