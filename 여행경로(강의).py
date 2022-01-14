def solution(tickets):
    answer = []
    routes = {}

    for i in tickets:
        routes[i[0]] = routes.get(i[0], []) + [i[1]]
    for i in routes:
        routes[i].sort(reverse = True)
    path=[]
    stack = ["ICN"]
    while stack: # 스택 사용 이유: 쌓아온 경로 추적
        now = stack[-1]
        if now not in routes or len(routes[now])==0:
            path.append(stack.pop())
        else:
            stack.append(routes[now].pop())
    answer = path[::-1]
    return answer
