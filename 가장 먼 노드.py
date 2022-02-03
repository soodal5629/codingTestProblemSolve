import heapq
def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    cost = [1e9] * (n+1)
    cost[1] = 0
    q= []
    for i in edge:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)
        q.append((1,1))
    while q:
        c, start = heapq.heappop(q)
        for i in graph[start]:
            if cost[i]>cost[start]+c:
                cost[i] = cost[start]+1
                heapq.heappush(q, (cost[i]+1, i))
    maxi = max(cost[1:])
    answer = cost.count(maxi)
    return answer
