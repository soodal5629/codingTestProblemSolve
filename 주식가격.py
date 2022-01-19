from collections import deque
def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        now = q.popleft()
        flag = False
        cnt = 0
        for i in q:
            cnt +=1
            if now > i:
                break
        answer.append(cnt)
    return answer
