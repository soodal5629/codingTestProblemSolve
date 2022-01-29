from collections import deque
def solution(routes):
    answer = 1
    routes.sort(key = lambda x:x[-1]) #정렬 이렇게 꼭 해줘야 함...
    routes = deque(routes)
    q = deque()
    q.append(routes.popleft())
    while routes:
        top_end = q[-1][1]
        push_start, push_end = routes.popleft()
        if push_start> top_end:
            q.pop()
            answer+=1
            q.append([push_start, push_end])
    return answer
