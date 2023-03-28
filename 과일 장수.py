from collections import deque
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    d = deque(score)
    while len(d) >= m:
        cnt = 0
        while len(d)>0 and cnt < m:
            temp = d.popleft()
            if cnt == m-1:
                answer += (m * temp) 
            cnt+=1
    return answer
