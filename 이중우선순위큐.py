import heapq
def solution(operations):
    answer = []
    q = []

    mini = 1e9
    maxi = -1e9
    
    for i in operations:
        if i[0]== ("I"): 
            q.append(int(i[2:]))
        elif i == ("D -1") and q:
            heapq.heappop(q)
        else:
            if q:
                temp_q = []   
                for j in q:
                    temp_q.append(-j)
                heapq.heapify(temp_q)
                temp = -(heapq.heappop(temp_q))
                for k in range(len(q)):
                    if q[k] == temp:
                        del q[k]
                        break
        heapq.heapify(q)
    if len(q) == 0:
        answer = [0,0]
    else:
        mini = min(heapq.heappop(q), mini)
        q2 = []
        for j in q:
            q2.append(-j)
        heapq.heapify(q2)
        maxi = max(-(heapq.heappop(q2)), maxi)
        answer = [maxi, mini]
    return answer
