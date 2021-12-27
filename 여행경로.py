# 인터넷 참고함
from collections import defaultdict
def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for key, value in tickets:
        routes[key].append(value)
    for key, value in tickets:
        routes[key].sort(reverse = True)
    stack = ["ICN"]
    while stack:
        temp = stack[-1]
        if routes[temp]:
            stack.append(routes[temp].pop())
        else:
            answer.append(stack.pop())
    answer.reverse()
    return answer
