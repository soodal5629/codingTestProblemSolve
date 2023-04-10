import heapq
def solution(k, score):
    answer = []
    q = []
    for i in range(k):
        if i < len(score):
            heapq.heappush(q, score[i])
            answer.append(min(score[:i+1]))
        else:
            return answer
    
    for i in range(k, len(score)):
        temp = heapq.heappop(q)
        v = score[i]
        if temp < v:
            heapq.heappush(q, v)
            temp2 = heapq.heappop(q)
            answer.append(temp2)
            heapq.heappush(q, temp2)
        else:
            answer.append(temp)
            heapq.heappush(q, temp)
    return answer
