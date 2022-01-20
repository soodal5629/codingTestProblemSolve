import heapq
def solution(jobs):
    answer = 0
    n = len(jobs)
    
    heapq.heapify(jobs)
    start, take =heapq.heappop(jobs)
    now_time = (start+take)
    answer = take
    
    while jobs:
        temp = []
        for i in jobs:
            temp.append((i[1],i[0]))
        heapq.heapify(temp)
        cnt = 0
        while temp:
            if now_time<temp[0][1]:
                heapq.heappop(temp)    
            else:
                cnt +=1
                take, start = heapq.heappop(temp)
                for i in range(len(jobs)):
                    if jobs[i][0] == start and jobs[i][1] == take:
                        del jobs[i] # 리스트에서 삭제
                        break
                answer += (now_time + take - start)
                now_time = now_time + take
                break
        if cnt == 0: now_time = jobs[0][0]
        heapq.heapify(jobs)
    answer = answer//n
    return answer
